import sys
import time
from . import utimezone

_isupy = True if sys.implementation.name == "micropython" else False

WEEKDAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']


def _mktime(year: int, month: int, day: int, hour: int, min: int, sec: int) -> int:
    """
    Reference: https://www.geeksforgeeks.org/python-time-mktime-method/

    Don't use this directly. Provided for use within this class.
    A platform safe mktime, since unix and upython have slightly different versions
    upython the tuple is (y,m,d,h,m,s,wk,yd)
    Unix python the tuple is (y,m,d,h,m,s,wk,yd,dst)
    month: 1-12
    day: 1-31
    hour:0-23
    minute:0-59
    sec: 0-61
    dow: 0-6. Monday == 0
    yd: 1-366
    """
    if _isupy:
        return int(time.mktime((year, month, day, hour, min, sec, None, None)))  # type: ignore [arg-type]
    else:
        return int(time.mktime((year, month, day, hour, min, sec, -1, -1, -1)))



class TZTime:
    """
    A simpleencapsulated time value, with an optional included TimeZone.
    This is an Immutable class.  All alteration methods return a new instance.
    That allows for easy daisy chaining too.
    The default constructor creates a "now()" instance, based on the system clock.
    It's assumed the system clock creates "zulu/UTC" time instances.  The best way to
    use this class is to in fact have your system clock set to UTC time.
    """

    def __init__(self, t: int | None = None, tz: utimezone.Timezone | None = None):
        """
        Create a new instance of a TZTime object.
        Defaults to now() at Zulu if no args are provided.
        time.time() is used when no t value is provided.
        your system must produce UTC time for this default to be
        effective.
        Use the class TZTime.create() method to create a specific time value.
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
        """
        Create an instance of now @ UTC
        """
        return TZTime()


    @staticmethod
    def create(year: int = 0, month: int = 0, day: int = 0, hour: int = 0, min: int = 0, sec: int = 0, tz: utimezone.Timezone | None = None) -> 'TZTime':
        """
        Create a new instance with the given time values, and specific timezone. A None tz is treated like Zulu/UTC

        month: 1-12

        day: 1-31

        hour: 0-23

        min: 0-59

        sec: 0-61
        """
        t = _mktime(year=year, month=month, day=day, hour=hour, min=min, sec=sec)
        return TZTime(t, tz)


    def isDst(self) -> bool:
        """
        Return if this time, and the given timezone, is a DST time or not.
        """
        if self._tz is None:
            return False
        else:
            return self._tz.locIsDST(self._time)


    def __str__(self) -> str:
        """
        Return the ISO8601 formatted string of this time
        """
        return self.toISO8601()


    def __repr__(self) -> str:
        """
        Return the ISO8601 formatted string of this time
        """
        return self.toISO8601()


    def __eq__(self, other) -> bool:
        """
        [==] Operator
        """
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time == other.toUTC()._time

    def __ne__(self, other) -> bool:
        """
        [!=] Operator
        """
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time != other.toUTC()._time


    def __gt__(self, other) -> bool:
        """
        [>] Operator
        """
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time > other.toUTC()._time


    def __lt__(self, other) -> bool:
        """
        [<] Operator
        """
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time < other.toUTC()._time

    def __ge__(self, other) -> bool:
        """
        [>=] Operator
        """
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time >= other.toUTC()._time


    def __le__(self, other) -> bool:
        """
        [<=] Operator
        """
        if not isinstance(other, TZTime):
            return False
        return self.toUTC()._time <= other.toUTC()._time


    def _gmtime(self) -> tuple:
        """
        Return the the underlying structured time tuple.
        We fetch the localtime, because on micropython, this is always the same as gmtime due to the lack of tz capacity.
        On unix python, gmtime converts for us, and we dont' want that.  So, localtime it is.
        """
        if self._stime is None:
            self._stime = time.localtime(self._time)
        return self._stime


    def toISO8601(self) -> str:
        """
        Generate a ISO8601 formatted string.
        """
        return toISO8601(self._time, self._tz)


    def year(self) -> int:
        """
        Get the Year
        """
        return self._gmtime()[0]


    def month(self) -> int:
        """
        Get the Month [1-12]
        """
        return self._gmtime()[1]


    def day(self) -> int:
        """
        Get the Day of the Month [1-31]
        """
        return self._gmtime()[2]


    def hour(self) -> int:
        """
        Get the Hour of the Dat 0-23
        """
        return self._gmtime()[3]


    def minute(self) -> int:
        """
        Get the Minute of the Hour [0-59]
        """
        return self._gmtime()[4]


    def second(self) -> int:
        """
        Get the second of the minute [0-59] (actually 0-61 if you account for leap-seconds and the like)
        """
        return self._gmtime()[5]


    def time(self) -> int:
        """
        Return the raw unix time value. Seconds since EPOCH (Jan 1 2000 on upy devices)
        """
        return self._time


    def tz(self) -> utimezone.Timezone | None:
        """
        Get the TimeZone. Returns None for UTC
        """
        return self._tz


    def toTimezone(self, tz: utimezone.Timezone | None) -> 'TZTime':
        """
        Convert this time, to the new timezone.
        If the new TZ is None, this is converted to UTC.
        This will alter the time to the new TimeZone.
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


    def plusYears(self, years: int) -> 'TZTime':
        """
        Add x years to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0] + years, gm[1], gm[2], gm[3], gm[4], gm[5])
        return TZTime(nt, self._tz)


    def plusMonths(self, months: int) -> 'TZTime':
        """
        Add x months to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1] + months, gm[2], gm[3], gm[4], gm[5])
        return TZTime(nt, self._tz)


    def plusDays(self, days: int) -> 'TZTime':
        """
        Add x days to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2] + days, gm[3], gm[4], gm[5])
        return TZTime(nt, self._tz)


    def plusHours(self, hours: int) -> 'TZTime':
        """
        Add x hours to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3] + hours, gm[4], gm[5])
        return TZTime(nt, self._tz)


    def plusMinutes(self, minutes: int) -> 'TZTime':
        """
        Add x minutes to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3], gm[4] + minutes, gm[5])
        return TZTime(nt, self._tz)


    def plusSeconds(self, seconds: int) -> 'TZTime':
        """
        Add x seconds to a time value.
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3], gm[4], gm[5] + seconds)
        return TZTime(nt, self._tz)


    def withMinuts(self, minutes: int) -> 'TZTime':
        """
        Set the minutes value
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3], minutes, gm[5])
        return TZTime(nt, self._tz)


    def withSeconds(self, seconds: int) -> 'TZTime':
        """
        Set the seconds value
        """
        gm = self._gmtime()
        nt = _mktime(gm[0], gm[1], gm[2], gm[3], gm[4], seconds)
        return TZTime(nt, self._tz)


    def withTimezone(self, tz: utimezone.Timezone) -> 'TZTime':
        """
        Sets the timezone, making no changes to the time value.
        You can also clear the timezone to UTC by passing None.
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
