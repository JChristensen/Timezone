import sys
import time
from . import utimezone

_utime = True if sys.implementation.name == "micropython" else False

WEEKDAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']


def _mktime(y: int, m: int, d: int, h: int, min: int, s: int) -> int:
    """
    A platform safe mktime, since unix and upython have slightly different versions
    upython the tuple is (y,m,d,h,m,s,wk,yd)
    Unix python the tuple is (y,m,d,h,m,s,wk,yd,dst)
    """
    if _utime:
        return int(time.mktime((y, m, d, h, min, s, None, None)))  # type: ignore [arg-type]
    else:
        return int(time.mktime((y, m, d, h, min, s, -1, -1, -1)))


class TZTime:
    """
    A simple encapsulated time value, with an optional included TimeZone.
    This is Immutable class.  All alteration methods return a new instance.
    That allows for easy daisy chaining too.
    The default constructor creates a "now()" instance, based on the system clock.
    It's assumed the system clock creates "zulu/UTC" time instances.
    If not
    returns a new instance
    """

    def __init__(self, t: int | None = None, tz: utimezone.Timezone | None = None):
        """
        Create a new instance of a TZTime object.
        Defaults to now() at Zulu if no values provided.
        time.time() is used when no t value is provided.
        your system must produce UTC time for this default to be
        effective.
        """

        # The unix "time" instance
        if t is None:
            self._time: int = int(time.time())
        else:
            assert isinstance(t, int), f"t must be an int, received [{t.__class__}]"
            self._time = t

        # The structured time. Calculated only the 1st time it's needed
        self._stime: time.struct_time | None = None

        # The TimeZone
        self._tz = tz


    @staticmethod
    def now() -> 'TZTime':
        return TZTime()


    @staticmethod
    def create(y: int = 0, m: int = 0, d: int = 0, h: int = 0, min: int = 0, s: int = 0, tz: utimezone.Timezone | None = None) -> 'TZTime':
        """
        Create a new instnace with the given time values, and specific timezone. A None tz is treated like Zulu/UTC
        """
        t = _mktime(y, m, d, h, min, s)
        return TZTime(t, tz)


    def __str__(self):
        """
        Return the ISO8601 of this time
        """
        return self.toISO8601()


    def __repr__(self) -> str:
        return self.toISO8601()


    def __eq__(self, other) -> bool:
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time == other.toUTC()._time

    def __ne__(self, other) -> bool:
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time != other.toUTC()._time


    def __gt__(self, other) -> bool:
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time > other.toUTC()._time


    def __lt__(self, other) -> bool:
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time < other.toUTC()._time

    def __ge__(self, other) -> bool:
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time >= other.toUTC()._time


    def __le__(self, other) -> bool:
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time <= other.toUTC()._time


    def _gmtime(self) -> tuple:
        """
        Return the structured time tuple.
        """
        if self._stime is None:
            self._stime = time.localtime(self._time)
        return self._stime


    def toISO8601(self) -> str:
        return toISO8601(self._time, self._tz)


    def year(self) -> int:
        return self._gmtime()[0]


    def month(self) -> int:
        """
        1-12
        """
        return self._gmtime()[1]


    def day(self) -> int:
        """
        1-31
        """
        return self._gmtime()[2]


    def hour(self) -> int:
        """
        0-23
        """
        return self._gmtime()[3]


    def minute(self) -> int:
        """
        0-59
        """
        return self._gmtime()[4]


    def second(self) -> int:
        """
        0-59 (actually 0-61)
        """
        return self._gmtime()[5]


    def time(self) -> int:
        """
        Return the raw unix time value
        """
        return self._time


    def tz(self) -> utimezone.Timezone | None:
        return self._tz


    def toTimezone(self, tz: utimezone.Timezone) -> 'TZTime':
        """
        Convert this time, to the new timezone.
        If the new TZ is None, this is covnerted to UTC
        """
        z = self.toUTC()
        if tz:
            t = tz.toLocal(z._time)
            return TZTime(t, tz)
        else:
            return z


    def toUTC(self) -> 'TZTime':
        """
        convert this time to UTC
        """
        t = self._time
        if self._tz:
            t = self._tz.toUTC(t)
        return TZTime(t, None)


    def secondsBetween(self, other: 'TZTime') -> int:
        """
        return the number of seconds between this, and the other time
        """
        thisZ = self.toUTC()
        otherZ = other.toUTC()
        return otherZ._time - thisZ._time


    def plusYears(self, years: int):
        """
        Add x years to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0] + years, gm[1], gm[2], gm[3], gm[4], gm[5])
        return TZTime(nt, self._tz)


    def plusMonths(self, months: int):
        """
        Add x months to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1] + months, gm[2], gm[3], gm[4], gm[5])
        return TZTime(nt, self._tz)


    def plusDays(self, days: int):
        """
        Add x days to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2] + days, gm[3], gm[4], gm[5])
        return TZTime(nt, self._tz)


    def plusHours(self, hours: int):
        """
        Add x hours to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3] + hours, gm[4], gm[5])
        return TZTime(nt, self._tz)


    def plusMinutes(self, minutes: int):
        """
        Add x minutes to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3], gm[4] + minutes, gm[5])
        return TZTime(nt, self._tz)


    def plusSeconds(self, seconds: int):
        """
        Add x seconds to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3], gm[4], gm[5] + seconds)
        return TZTime(nt, self._tz)


    def withMinuts(self, minutes: int):
        """
        Set the minutes value
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3], minutes, gm[5])
        return TZTime(nt, self._tz)


    def withSeconds(self, seconds: int):
        """
        Set the seconds value
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3], gm[4], seconds)
        return TZTime(nt, self._tz)


    def withTimezone(self, tz: utimezone.Timezone) -> 'TZTime':
        """
        Sets the timezone, making no changes to the time value.
        You can also clear the timzone by passing None
        """
        return TZTime(self._time, tz)


def toISO8601(t: int, tz: utimezone.Timezone | None = None) -> str:
    """
    Take the unix time t, and convert it into an ISO8601 string.
    Use the tz as the Zone designator.  None for Zulu or Local.
    The tz does not convert the time, it adds the correct offset value
    used at the end.
    """

    assert t is not None, "t can't be None"
    assert isinstance(t, int), f"t must be an int. Received [{t.__class__}]"

    if tz is not None:
        assert isinstance(tz, utimezone.Timezone), f"TZ must be None for Zulu, or a utimezone.Timezone instance. Got [{tz.__class__}]"
        offset = 0
        if tz.locIsDST(t):
            offset = tz._dst.offset
        else:
            offset = tz._std.offset

        offsetHours = int(offset / 60)
        offsetMinutes = int(offset % 60)
        offsetDir = "+" if offsetHours > 0 else "-"
        offsetHours = abs(offsetHours)
        tzstr = f"{offsetDir}{offsetHours:02d}:{offsetMinutes:02d}"
    else:
        tzstr = "Z"

    g = time.gmtime(t)
    iso = f"{g[0]:04d}-{g[1]:02d}-{g[2]:02d}T{g[3]:02d}:{g[4]:02d}:{g[5]:02d}{tzstr}"
    return iso


# Access to the EPOCH value. Unlike non-micropython devices which use an EPOCH of Jan 1 1970.
# The Micropython EPOCH is Jan 1 2000
EPOCH = TZTime.create(2000, 1, 1, 0, 0, 0, None)
