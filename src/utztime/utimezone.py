"""
Python Timezone Library
Port of the Arduino Timezone Library by Jack Christensen Mar 2012
Intended to be used on micropython devices.

Python Timezone Library Copyright (C) 2018 by Jack Christensen and
licensed under GNU GPL v3.0, https://www.gnu.org/licenses/gpl.html

**See tz/us.py** for examples.

Not Currently Thread Safe. Uses an internal field state tracked by year.  I'll fix this in the near future.
"""
import time
import utztime.tztime
import sys

# week values for TimeChangeRule
LAST = -1
FIRST = 0
SECOND = 1
THIRD = 2
FOURTH = 3

# dow values for TimeChangeRule  https://www.geeksforgeeks.org/python-time-mktime-method/
MON = 0
TUE = 1
WED = 2
THU = 3
FRI = 4
SAT = 5
SUN = 6

# month values for TimeChangeRule  https://www.geeksforgeeks.org/python-time-mktime-method/
JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12

SECS_PER_MIN = 60
SECS_PER_DAY = 24 * 60 * 60
DAYS_PER_WEEK = 7

# Micropython has a Epoch of 2000, not 1970
EPOCH_YEAR = time.gmtime(0)[0]


class TimeChangeRule:
    """
    Simple data structure to define a change over rule
    """

    def __init__(self,
                 abbrev: str,
                 whichDow: int,
                 dow: int,
                 month: int,
                 hour: int,
                 offset: int):
        """
        abbrev: 5 chars max. eg. DST, EDT, PST...
        whichDow: Which day of our dow? see internal FIRST, SECOND, THIRD, etc
        dow: day of week, see internal SUN, MON, TUE.. ETC
        month: Which Month.  see internal JAN, FEB, MAR.. etc
        hour: # 0-23
        offset: The timezone offset from UTC in minutes
        """
        self.abbrev = abbrev
        self.whichDow = whichDow
        self.dow = dow
        self.month = month
        self.hour = hour
        self.offset = offset


    def clone(self) -> 'TimeChangeRule':
        """
        Create a clone of this rule
        """
        return TimeChangeRule(abbrev=self.abbrev, whichDow=self.whichDow, dow=self.dow, month=self.month, hour=self.hour, offset=self.offset)


    def __eq__(self, other) -> bool:
        """
        [==] Operator.  Compares all fields except the abbrev.  Used in the unit test that attempts
            to find re-defined rules.
        """
        if not isinstance(other, TimeChangeRule):
            return False
        return self.whichDow == other.whichDow and \
            self.dow == other.dow and \
            self.month == other.month and \
            self.hour == other.hour and \
            self.offset == other.offset


    def __ne__(self, other) -> bool:
        """
        [!=] Operator.
        """
        return not self == other


    def toTime(self, yr: int) -> int:
        """
        Convert using this time change rule to a time value
        for the given year.
        """

        # 1st, 2nd.. etc. This month.  Last.. start with next month.
        month = self.month if self.whichDow > LAST else self.month + 1

        # Start by finding the first day of the rule month. And what dow it falls on.
        t = utztime.tztime._mktime(yr, month, 1, self.hour, 0, 0)
        tDow = time.gmtime(t)[6]

        # How many days to the 1st occurrence of the desired day. The +1 at the end is because pythons gmtime returns 0-6 for dow above
        daysToRuleDow = (self.dow - tDow + DAYS_PER_WEEK) % DAYS_PER_WEEK + 1

        # Add (or subtract if this is the last, and we're in next month) the occurrence multiplier
        daysToRuleDow += (DAYS_PER_WEEK * self.whichDow)

        # re-generate t with a new day specifier
        t = utztime.tztime._mktime(yr, month, daysToRuleDow, self.hour, 0, 0)

        return t


class Timezone:
    """
    A Immutable TimeZone rule definition.
    A Daylight Savings Time rule, and a Standard Rule.
    """

    def __init__(self, name: str, std: TimeChangeRule, dst: TimeChangeRule | None):
        """
        name - name of this timezone.  eg.  America/Chicago
        stdStart - The start of Standard Time Rule.
        dstStart - Optional. The start of Daylight Savings Time Rule. Set to None if this TZ observes only standard time.
        """
        self._name = name
        self._std = std
        self._dst = dst if dst is not None else std
        self._dstLoc = 0
        self._stdLoc = 0
        self._dstUTC = 0
        self._stdUTC = 0


    def clone(self, name: str, shallow: bool = False) -> 'Timezone':
        """
        Create a complete copy of this timezone.
        Provide a new-name for this clone.
        shallow will not clone the rules, but instead use the same instance.
        This has the benefit of being lighter weight on memory, but running the
        risk of side-affects if used incorrectly
        """
        std = self._std if shallow else self._std.clone()
        dst = self._dst if shallow else self._dst.clone()
        return Timezone(std=std, dst=dst, name=name)


    def link(self, name: str) -> 'Timezone':
        """
        Shortcut to create a shallow clone
        """
        return self.clone(name, shallow=True)


    def __str__(self) -> str:
        """
        Returns the "name" of this timezone
        """
        return self.getName()


    def __gt__(self, other) -> bool:
        """
        [>] Operator. Compares the StandardTime offset
        """
        if not isinstance(other, Timezone):
            return False
        return self._std.offset > other._std.offset


    def __lt__(self, other) -> bool:
        """
        [<] Operator. Compares the StandardTime offset
        """
        if not isinstance(other, Timezone):
            return False
        return self._std.offset < other._std.offset

    def __ge__(self, other) -> bool:
        """
        [>=] Operator. Compares the StandardTime offset
        """
        if not isinstance(other, Timezone):
            return False
        return self._std.offset >= other._std.offset


    def __le__(self, other) -> bool:
        """
        [<=] Operator. Compares the StandardTime offset
        """
        if not isinstance(other, Timezone):
            return False
        return self._std.offset <= other._std.offset


    def __eq__(self, other) -> bool:
        """
        [==] Operator. Compares the 2 std & dst rules. Ignores the name differences
        """
        if not isinstance(other, Timezone):
            return False
        return self._std == other._std and self._dst == other._dst


    def __ne__(self, other) -> bool:
        """
        [!=] Operator. Compares the StandardTime offset
        """
        if not isinstance(other, Timezone):
            return False
        return not self == other


    def getName(self):
        """
        Return the name of this timezone.
        """
        return self._name


    def _calcTimeChanges(self, yr: int):
        """
        Calculate the DST and standard time change points for the given
        given year as local and UTC time_t values.
        """
        self._dstLoc = self._dst.toTime(yr)
        self._stdLoc = self._std.toTime(yr)
        self._dstUTC = self._dstLoc - self._std.offset * SECS_PER_MIN
        self._stdUTC = self._stdLoc - self._dst.offset * SECS_PER_MIN



    def toLocal(self, utc: int) -> int:
        """
        Convert the given UTC time to local time, standard or
        daylight time, as appropriate.
        """

        # recalculate the time change points if needed
        year: int = time.gmtime(utc)[0]
        dstYear: int = time.gmtime(self._dstUTC)[0]

        if year != dstYear:
            self._calcTimeChanges(year)

        if self.utcIsDST(utc):
            return utc + self._dst.offset * SECS_PER_MIN
        else:
            return utc + self._std.offset * SECS_PER_MIN


    def toUTC(self, local: int) -> int:
        """
        Convert the given local time to UTC time.

        WARNING:
        This function is provided for completeness, but should seldom be
        needed and should be used sparingly and carefully.

        Ambiguous situations occur after the Standard-to-DST and the
        DST-to-Standard time transitions. When changing to DST, there is
        one hour of local time that does not exist, since the clock moves
        forward one hour. Similarly, when changing to standard time, there
        is one hour of local times that occur twice since the clock moves
        back one hour.

        This function does not test whether it is passed an erroneous time
        value during the Local -> DST transition that does not exist.
        If passed such a time, an incorrect UTC time value will be returned.

        If passed a local time value during the DST -> Local transition
        that occurs twice, it will be treated as the earlier time, i.e.
        the time that occurs before the transition.

        Calling this function with local times during a transition interval
        should be avoided!
        """
        # recalculate the time change points if needed
        year: int = time.gmtime(local)[0]
        dstYear: int = time.gmtime(self._dstLoc)[0]
        if year != dstYear:
            self._calcTimeChanges(year)

        if self.locIsDST(local):
            return local - self._dst.offset * SECS_PER_MIN
        else:
            return local - self._std.offset * SECS_PER_MIN


    def utcIsDST(self, utc: int) -> bool:
        """
        Determine whether the given UTC time is within the DST interval
        or the Standard time interval
        """
        # recalculate the time change points if needed
        year: int = time.gmtime(utc)[0]
        dstYear: int = time.gmtime(self._dstUTC)[0]
        if year != dstYear:
            self._calcTimeChanges(year)

        if self._stdUTC == self._dstUTC:       # daylight time not observed in this tz
            return False
        elif self._stdUTC > self._dstUTC:      # northern hemisphere
            return utc >= self._dstUTC and utc < self._stdUTC
        else:                                   # southern hemisphere
            return not (utc >= self._stdUTC and utc < self._dstUTC)

    def utcIsSTD(self, utc: int) -> bool:
        """
        Convenient wrapper to utcIsDST
        """
        return not self.utcIsDST(utc)


    def locIsDST(self, local: int) -> bool:
        """
        Determine whether the given Local time is within the DST interval
        or the Standard time interval.
        """
        # recalculate the time change points if needed
        year: int = time.gmtime(local)[0]
        dstYear: int = time.gmtime(self._dstLoc)[0]
        if year != dstYear:
            self._calcTimeChanges(year)

        if self._stdUTC == self._dstUTC:       # daylight time not observed in this tz
            return False
        elif self._stdLoc > self._dstLoc:      # northern hemisphere
            return local >= self._dstLoc and local < self._stdLoc
        else:                                  # southern hemisphere
            return not (local >= self._stdLoc and local < self._dstLoc)


    def locIsSTD(self, utc: int) -> bool:
        """
        Convenient wrapper to locIsDST
        """
        return not self.locIsDST(utc)
