"""
Python Timezone Library  
Port of the Arduino Timezone Library by Jack Christensen Mar 2012 
Intended to be used on micropython devices.

Python Timezone Library Copyright (C) 2018 by Jack Christensen and
licensed under GNU GPL v3.0, https://www.gnu.org/licenses/gpl.html 
"""
import utime

# week values for TimeChangeRule
LAST      = 0
FIRST     = 1
SECOND    = 2
THIRD     = 3
FOURTH    = 4

# dow values for TimeChangeRule
SUN = 1
MON = 2
TUE = 3
WED = 4
THU = 5
FRI = 6
SAT = 7

# month values for TimeChangeRule
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

class TimeChangeRule:
    """
    Simple data structure to define a change over rule
    """
    abbrev: str
    week: int
    dow: int
    month: int
    hour: int
    offset: int

    def __init__(self, 
        abbrev: str,    # five chars max
        week: int,      # First, Second, Third, Fourth, or Last week of the month
        dow: int,       # day of week, 1=Sun, 2=Mon, ... 7=Sat
        month: int,     # 1=Jan, 2=Feb, ... 12=Dec
        hour: int,      # 0-23
        offset: int):     # offset from UTC in minutes
        self.abbrev = abbrev
        self.week = week
        self.dow = dow
        self.month = month
        self.hour = hour
        self.offset = offset
    

class Timezone:

    _std: TimeChangeRule = None
    _dst: TimeChangeRule = None
    _dstLoc = 0
    _stdLoc = 0
    _dstUTC = 0
    _stdUTC = 0
    _name = ""

    def __init__(self, stdStart: TimeChangeRule, dstStart: TimeChangeRule, name = None):
        """
        stdStart - The start of Standard Time Rule
        dstStart - The start of Daylight Savings Time Rule
        name - Optional name of this timezone
        """
        self._name = name
        self.setRules(stdStart, dstStart)
        
    
    def _calcTimeChanges(self, yr: int):
        """
        Calculate the DST and standard time change points for the given
        given year as local and UTC time_t values.
        """
        self._dstLoc = self._toTime(self._dst, yr);
        self._stdLoc = self._toTime(self._std, yr);
        self._dstUTC = self._dstLoc - self._std.offset * SECS_PER_MIN
        self._stdUTC = self._stdLoc - self._dst.offset * SECS_PER_MIN


    def _toTime(self, r: TimeChangeRule, yr: int) -> int:
        """
        Convert the given time change rule to a time value  
        for the given year.   
        """

        m = r.month             # temp copies of r.month and r.week
        w = r.week
        if w == 0:              # is this a "Last week" rule?
            m += 1
            if m > 12:          # yes, for "Last", go to the next month
                m = 1
                yr += 1
            w = 1;              # and treat as first week of next month, subtract 7 days later


        t = utime.mktime( (yr, m, 1, r.hour, 0, 0, 0, 0) )
        tWeekday = utime.gmtime(t)[6]
       
        # add offset from the first of the month to r.dow, and offset for the given week
        t += ( (r.dow - tWeekday + 7) % 7 + (w - 1) * 7 ) * SECS_PER_DAY
        # back up a week if this is a "Last" rule
        if (r.week == 0):
             t -= 7 * SECS_PER_DAY

        return t


    def toLocal(self, utc: int) -> int:
        """
        Convert the given UTC time to local time, standard or                *
        daylight time, as appropriate.                                       *
        """

        # recalculate the time change points if needed
        year = utime.gmtime(utc)[0]
        dstYear = utime.gmtime(self._dstUTC)
        
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
        the time that occurs before the transistion.                         
                                                                             
        Calling this function with local times during a transition interval  
        should be avoided!                                                   
        """
        # recalculate the time change points if needed
        year = utime.gmtime(local)[0]
        dstYear = utime.gmtime(self._dstLoc)
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
        year = utime.gmtime(utc)[0]
        dstYear = utime.gmtime(self._dstUTC)
        if year != dstYear:
            self._calcTimeChanges(year)

        if self._stdUTC == self._dstUTC:       # daylight time not observed in this tz
            return False
        elif self._stdUTC > self._dstUTC:      # northern hemisphere
            return utc >= self._dstUTC and utc < self._stdUTC
        else:                                   # southern hemisphere
            return not (utc >= self._stdUTC and utc < self._dstUTC)


    def locIsDST(self, local: int) -> bool:
        """
        Determine whether the given Local time is within the DST interval 
        or the Standard time interval.
        """
        # recalculate the time change points if needed
        year = utime.gmtime(local)[0]
        dstYear = utime.gmtime(self._dstLoc)
        if year != dstYear:
            self._calcTimeChanges(year)

        if self._stdUTC == self._dstUTC:       # daylight time not observed in this tz
            return False
        elif self._stdLoc > self._dstLoc:      # northern hemisphere
            return local >= self._dstLoc and local < self._stdLoc
        else:                                  # southern hemisphere
            return not (local >= self._stdLoc and local < self._dstLoc)

    def setRules(self, stdStart: TimeChangeRule, dstStart: TimeChangeRule):
        """
        Update the daylight and standard time rules from RAM.     
        """
        self._std = stdStart
        self._dst = dstStart
        self._dstLoc = 0
        self._stdLoc = 0
        self._dstUTC = 0
        self._stdUTC = 0
        
