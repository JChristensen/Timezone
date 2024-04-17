# Table of Contents

* [utztime](#utztime)
* [utztime.utimezone](#utztime.utimezone)
  * [TimeChangeRule](#utztime.utimezone.TimeChangeRule)
    * [\_\_init\_\_](#utztime.utimezone.TimeChangeRule.__init__)
  * [Timezone](#utztime.utimezone.Timezone)
    * [\_\_init\_\_](#utztime.utimezone.Timezone.__init__)
    * [\_\_str\_\_](#utztime.utimezone.Timezone.__str__)
    * [\_\_gt\_\_](#utztime.utimezone.Timezone.__gt__)
    * [\_\_lt\_\_](#utztime.utimezone.Timezone.__lt__)
    * [\_\_ge\_\_](#utztime.utimezone.Timezone.__ge__)
    * [\_\_le\_\_](#utztime.utimezone.Timezone.__le__)
    * [\_\_eq\_\_](#utztime.utimezone.Timezone.__eq__)
    * [\_\_ne\_\_](#utztime.utimezone.Timezone.__ne__)
    * [getName](#utztime.utimezone.Timezone.getName)
    * [toLocal](#utztime.utimezone.Timezone.toLocal)
    * [toUTC](#utztime.utimezone.Timezone.toUTC)
    * [utcIsDST](#utztime.utimezone.Timezone.utcIsDST)
    * [locIsDST](#utztime.utimezone.Timezone.locIsDST)
* [utztime.utzlist](#utztime.utzlist)
  * [getTimezones](#utztime.utzlist.getTimezones)
  * [getTimezoneNames](#utztime.utzlist.getTimezoneNames)
  * [getTimezone](#utztime.utzlist.getTimezone)
  * [setTimezone](#utztime.utzlist.setTimezone)
* [utztime.tztime](#utztime.tztime)
  * [TZTime](#utztime.tztime.TZTime)
    * [\_\_init\_\_](#utztime.tztime.TZTime.__init__)
    * [now](#utztime.tztime.TZTime.now)
    * [create](#utztime.tztime.TZTime.create)
    * [\_\_str\_\_](#utztime.tztime.TZTime.__str__)
    * [\_\_repr\_\_](#utztime.tztime.TZTime.__repr__)
    * [\_\_eq\_\_](#utztime.tztime.TZTime.__eq__)
    * [\_\_ne\_\_](#utztime.tztime.TZTime.__ne__)
    * [\_\_gt\_\_](#utztime.tztime.TZTime.__gt__)
    * [\_\_lt\_\_](#utztime.tztime.TZTime.__lt__)
    * [\_\_ge\_\_](#utztime.tztime.TZTime.__ge__)
    * [\_\_le\_\_](#utztime.tztime.TZTime.__le__)
    * [toISO8601](#utztime.tztime.TZTime.toISO8601)
    * [year](#utztime.tztime.TZTime.year)
    * [month](#utztime.tztime.TZTime.month)
    * [day](#utztime.tztime.TZTime.day)
    * [hour](#utztime.tztime.TZTime.hour)
    * [minute](#utztime.tztime.TZTime.minute)
    * [second](#utztime.tztime.TZTime.second)
    * [time](#utztime.tztime.TZTime.time)
    * [tz](#utztime.tztime.TZTime.tz)
    * [toTimezone](#utztime.tztime.TZTime.toTimezone)
    * [toUTC](#utztime.tztime.TZTime.toUTC)
    * [secondsBetween](#utztime.tztime.TZTime.secondsBetween)
    * [plusYears](#utztime.tztime.TZTime.plusYears)
    * [plusMonths](#utztime.tztime.TZTime.plusMonths)
    * [plusDays](#utztime.tztime.TZTime.plusDays)
    * [plusHours](#utztime.tztime.TZTime.plusHours)
    * [plusMinutes](#utztime.tztime.TZTime.plusMinutes)
    * [plusSeconds](#utztime.tztime.TZTime.plusSeconds)
    * [withMinuts](#utztime.tztime.TZTime.withMinuts)
    * [withSeconds](#utztime.tztime.TZTime.withSeconds)
    * [withTimezone](#utztime.tztime.TZTime.withTimezone)
  * [toISO8601](#utztime.tztime.toISO8601)

<a id="utztime"></a>

# utztime

Root package.

**To simply access the TZTime class**
```python
from utztime import TZTime
```

**Access to the time zone rules**
```python
from utztime.utimezone import TimeChangeRule, Timezone
```

**Access to the pre-defined list of timezones**
```python
import utztime.tzlist
```

There is a `EPOCH` const that can be used here if desired.  It is the uPython EPOCH of Jan 1 2000. Not the unix EPOCH of Jan 1 1970
```python
EPOCH
```

<a id="utztime.utimezone"></a>

# utztime.utimezone

Python Timezone Library
Port of the Arduino Timezone Library by Jack Christensen Mar 2012
Intended to be used on micropython devices.

Python Timezone Library Copyright (C) 2018 by Jack Christensen and
licensed under GNU GPL v3.0, https://www.gnu.org/licenses/gpl.html

**See utzlist.py** for examples.

<a id="utztime.utimezone.TimeChangeRule"></a>

## TimeChangeRule Objects

```python
class TimeChangeRule()
```

Simple data structure to define a change over rule

<a id="utztime.utimezone.TimeChangeRule.__init__"></a>

#### \_\_init\_\_

```python
def __init__(abbrev: str, week: int, dow: int, month: int, hour: int,
             offset: int)
```

abbrev: 5 chars max. eg. DST, EDT, PST...
week: First, Second, Third, Fourth, or Last week of the month
dow: day of week, 1=Sun, 2=Mon, ... 7=Sat
month: 1=Jan, 2=Feb, ... 12=Dec
hour: # 0-23
offset: The timezone offset from UTC in minutes

<a id="utztime.utimezone.Timezone"></a>

## Timezone Objects

```python
class Timezone()
```

A Immutable TimeZone rule definition.
A Daylight Savings Time rule, and a Standard Rule.

<a id="utztime.utimezone.Timezone.__init__"></a>

#### \_\_init\_\_

```python
def __init__(stdStart: TimeChangeRule,
             dstStart: TimeChangeRule,
             name: str | None = None)
```

stdStart - The start of Standard Time Rule
dstStart - The start of Daylight Savings Time Rule
name - Optional name of this timezone.  eg.  America/Chicago

<a id="utztime.utimezone.Timezone.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

Returns the "name" of this timezone

<a id="utztime.utimezone.Timezone.__gt__"></a>

#### \_\_gt\_\_

```python
def __gt__(other) -> bool
```

[>] Operator. Compares the StandardTime offset

<a id="utztime.utimezone.Timezone.__lt__"></a>

#### \_\_lt\_\_

```python
def __lt__(other) -> bool
```

[<] Operator. Compares the StandardTime offset

<a id="utztime.utimezone.Timezone.__ge__"></a>

#### \_\_ge\_\_

```python
def __ge__(other) -> bool
```

[>=] Operator. Compares the StandardTime offset

<a id="utztime.utimezone.Timezone.__le__"></a>

#### \_\_le\_\_

```python
def __le__(other) -> bool
```

[<=] Operator. Compares the StandardTime offset

<a id="utztime.utimezone.Timezone.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other) -> bool
```

[==] Operator. Compares the StandardTime offset

<a id="utztime.utimezone.Timezone.__ne__"></a>

#### \_\_ne\_\_

```python
def __ne__(other) -> bool
```

[!=] Operator. Compares the StandardTime offset

<a id="utztime.utimezone.Timezone.getName"></a>

#### getName

```python
def getName()
```

Return the name of this timezone.

<a id="utztime.utimezone.Timezone.toLocal"></a>

#### toLocal

```python
def toLocal(utc: int) -> int
```

Convert the given UTC time to local time, standard or
daylight time, as appropriate.

<a id="utztime.utimezone.Timezone.toUTC"></a>

#### toUTC

```python
def toUTC(local: int) -> int
```

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

<a id="utztime.utimezone.Timezone.utcIsDST"></a>

#### utcIsDST

```python
def utcIsDST(utc: int) -> bool
```

Determine whether the given UTC time is within the DST interval
or the Standard time interval

<a id="utztime.utimezone.Timezone.locIsDST"></a>

#### locIsDST

```python
def locIsDST(local: int) -> bool
```

Determine whether the given Local time is within the DST interval
or the Standard time interval.

<a id="utztime.utzlist"></a>

# utztime.utzlist

Simply a list of defined TimeZones you can include in your package, or just copy the one you want.

See the source file directly for a list of pre-defined TimeZones.

The timezones are stored in sort order of the offset value of the StandardTime of each zone.

```python
America_Newfoundland
America_Atlantic
America_Eastern
America_Central
America_Mountain
America_MountainNoDST
America_Pacific
America_Alaska
America_Hawaii
```

<a id="utztime.utzlist.getTimezones"></a>

#### getTimezones

```python
def getTimezones() -> list[tz.Timezone]
```

Return a COPY list of registered timezones. Sorted by Standard Time Offset (reverse) Highest to Lowest.

<a id="utztime.utzlist.getTimezoneNames"></a>

#### getTimezoneNames

```python
def getTimezoneNames() -> list[str]
```

Return a COPY list of the registered timezone names.  Sorted by Standard Time Offset (reverse) Highest to Lowest

<a id="utztime.utzlist.getTimezone"></a>

#### getTimezone

```python
def getTimezone(tzname: str) -> tz.Timezone | None
```

Find the timezone for the provided tz standard string.
This only references the pre-defined list of available timezones
within this module. This lookup is case insensitive.
Timezones are immutable.

<a id="utztime.utzlist.setTimezone"></a>

#### setTimezone

```python
def setTimezone(tz: tz.Timezone)
```

Set/Add to the internal list of available timezones.
This simply makes the provided timezone accessible
through the getTimezone() function

<a id="utztime.tztime"></a>

# utztime.tztime

<a id="utztime.tztime.TZTime"></a>

## TZTime Objects

```python
class TZTime()
```

A simpleencapsulated time value, with an optional included TimeZone.
This is an Immutable class.  All alteration methods return a new instance.
That allows for easy daisy chaining too.
The default constructor creates a "now()" instance, based on the system clock.
It's assumed the system clock creates "zulu/UTC" time instances.  The best way to
use this class is to in fact have your system clock set to UTC time.

<a id="utztime.tztime.TZTime.__init__"></a>

#### \_\_init\_\_

```python
def __init__(t: int | None = None, tz: utimezone.Timezone | None = None)
```

Create a new instance of a TZTime object.
Defaults to now() at Zulu if no args are provided.
time.time() is used when no t value is provided.
your system must produce UTC time for this default to be
effective.
Use the class TZTime.create() method to create a specific time value.

<a id="utztime.tztime.TZTime.now"></a>

#### now

```python
@staticmethod
def now() -> 'TZTime'
```

Create an instance of now @ UTC

<a id="utztime.tztime.TZTime.create"></a>

#### create

```python
@staticmethod
def create(year: int = 0,
           month: int = 0,
           day: int = 0,
           hour: int = 0,
           min: int = 0,
           sec: int = 0,
           tz: utimezone.Timezone | None = None) -> 'TZTime'
```

Create a new instance with the given time values, and specific timezone. A None tz is treated like Zulu/UTC

<a id="utztime.tztime.TZTime.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

Return the ISO8601 formatted string of this time

<a id="utztime.tztime.TZTime.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

Return the ISO8601 formatted string of this time

<a id="utztime.tztime.TZTime.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other) -> bool
```

[==] Operator

<a id="utztime.tztime.TZTime.__ne__"></a>

#### \_\_ne\_\_

```python
def __ne__(other) -> bool
```

[!=] Operator

<a id="utztime.tztime.TZTime.__gt__"></a>

#### \_\_gt\_\_

```python
def __gt__(other) -> bool
```

[>] Operator

<a id="utztime.tztime.TZTime.__lt__"></a>

#### \_\_lt\_\_

```python
def __lt__(other) -> bool
```

[<] Operator

<a id="utztime.tztime.TZTime.__ge__"></a>

#### \_\_ge\_\_

```python
def __ge__(other) -> bool
```

[>=] Operator

<a id="utztime.tztime.TZTime.__le__"></a>

#### \_\_le\_\_

```python
def __le__(other) -> bool
```

[<=] Operator

<a id="utztime.tztime.TZTime.toISO8601"></a>

#### toISO8601

```python
def toISO8601() -> str
```

Generate a ISO8601 formatted string.

<a id="utztime.tztime.TZTime.year"></a>

#### year

```python
def year() -> int
```

Get the Year

<a id="utztime.tztime.TZTime.month"></a>

#### month

```python
def month() -> int
```

Get the Month [1-12]

<a id="utztime.tztime.TZTime.day"></a>

#### day

```python
def day() -> int
```

Get the Day of the Month [1-31]

<a id="utztime.tztime.TZTime.hour"></a>

#### hour

```python
def hour() -> int
```

Get the Hour of the Dat 0-23

<a id="utztime.tztime.TZTime.minute"></a>

#### minute

```python
def minute() -> int
```

Get the Minute of the Hour [0-59]

<a id="utztime.tztime.TZTime.second"></a>

#### second

```python
def second() -> int
```

Get the second of the minute [0-59] (actually 0-61 if you account for leap-seconds and the like)

<a id="utztime.tztime.TZTime.time"></a>

#### time

```python
def time() -> int
```

Return the raw unix time value. Seconds since EPOCH (Jan 1 2000 on upy devices)

<a id="utztime.tztime.TZTime.tz"></a>

#### tz

```python
def tz() -> utimezone.Timezone | None
```

Get the TimeZone. Returns None for UTC

<a id="utztime.tztime.TZTime.toTimezone"></a>

#### toTimezone

```python
def toTimezone(tz: utimezone.Timezone) -> 'TZTime'
```

Convert this time, to the new timezone.
If the new TZ is None, this is converted to UTC.
This will alter the time to the new TimeZone.

<a id="utztime.tztime.TZTime.toUTC"></a>

#### toUTC

```python
def toUTC() -> 'TZTime'
```

convert this time to UTC

<a id="utztime.tztime.TZTime.secondsBetween"></a>

#### secondsBetween

```python
def secondsBetween(other: 'TZTime') -> int
```

return the number of seconds between this, and the other time

<a id="utztime.tztime.TZTime.plusYears"></a>

#### plusYears

```python
def plusYears(years: int) -> 'TZTime'
```

Add x years to a time value.

<a id="utztime.tztime.TZTime.plusMonths"></a>

#### plusMonths

```python
def plusMonths(months: int) -> 'TZTime'
```

Add x months to a time value.

<a id="utztime.tztime.TZTime.plusDays"></a>

#### plusDays

```python
def plusDays(days: int) -> 'TZTime'
```

Add x days to a time value.

<a id="utztime.tztime.TZTime.plusHours"></a>

#### plusHours

```python
def plusHours(hours: int) -> 'TZTime'
```

Add x hours to a time value.

<a id="utztime.tztime.TZTime.plusMinutes"></a>

#### plusMinutes

```python
def plusMinutes(minutes: int) -> 'TZTime'
```

Add x minutes to a time value.

<a id="utztime.tztime.TZTime.plusSeconds"></a>

#### plusSeconds

```python
def plusSeconds(seconds: int) -> 'TZTime'
```

Add x seconds to a time value.

<a id="utztime.tztime.TZTime.withMinuts"></a>

#### withMinuts

```python
def withMinuts(minutes: int) -> 'TZTime'
```

Set the minutes value

<a id="utztime.tztime.TZTime.withSeconds"></a>

#### withSeconds

```python
def withSeconds(seconds: int) -> 'TZTime'
```

Set the seconds value

<a id="utztime.tztime.TZTime.withTimezone"></a>

#### withTimezone

```python
def withTimezone(tz: utimezone.Timezone) -> 'TZTime'
```

Sets the timezone, making no changes to the time value.
You can also clear the timezone to UTC by passing None.

<a id="utztime.tztime.toISO8601"></a>

#### toISO8601

```python
def toISO8601(t: int, tz: utimezone.Timezone | None = None) -> str
```

Take the unix time t, and convert it into an ISO8601 string.
Use the tz as the Zone designator.  None for Zulu or Local.
The tz does not convert the time, it adds the correct offset value
used at the end.

