# Table of Contents

* [utztime](#utztime)
* [utztime.utimezone](#utztime.utimezone)
  * [TimeChangeRule](#utztime.utimezone.TimeChangeRule)
    * [\_\_init\_\_](#utztime.utimezone.TimeChangeRule.__init__)
    * [clone](#utztime.utimezone.TimeChangeRule.clone)
    * [\_\_eq\_\_](#utztime.utimezone.TimeChangeRule.__eq__)
    * [\_\_ne\_\_](#utztime.utimezone.TimeChangeRule.__ne__)
    * [toTime](#utztime.utimezone.TimeChangeRule.toTime)
  * [Timezone](#utztime.utimezone.Timezone)
    * [\_\_init\_\_](#utztime.utimezone.Timezone.__init__)
    * [clone](#utztime.utimezone.Timezone.clone)
    * [link](#utztime.utimezone.Timezone.link)
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
    * [utcIsSTD](#utztime.utimezone.Timezone.utcIsSTD)
    * [locIsDST](#utztime.utimezone.Timezone.locIsDST)
    * [locIsSTD](#utztime.utimezone.Timezone.locIsSTD)
* [utztime.utzlist](#utztime.utzlist)
  * [getTimezones](#utztime.utzlist.getTimezones)
  * [getTimezoneNames](#utztime.utzlist.getTimezoneNames)
  * [getTimezone](#utztime.utzlist.getTimezone)
  * [registerTimezone](#utztime.utzlist.registerTimezone)
  * [clear](#utztime.utzlist.clear)
* [utztime.tztime](#utztime.tztime)
  * [TZTime](#utztime.tztime.TZTime)
    * [\_\_init\_\_](#utztime.tztime.TZTime.__init__)
    * [now](#utztime.tztime.TZTime.now)
    * [create](#utztime.tztime.TZTime.create)
    * [isDst](#utztime.tztime.TZTime.isDst)
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
* [utztime.tz](#utztime.tz)
* [utztime.tz.us](#utztime.tz.us)
* [utztime.tz.bm](#utztime.tz.bm)
* [utztime.tz.ca](#utztime.tz.ca)

<a id="utztime"></a>

# utztime

Root package.

**To simply access the TZTime class**
```python
from utztime import TZTime
```

**Access to the timezone and rules classes**
```python
from utztime import TimeChangeRule, Timezone
```

**Access to the pre-defined list of timezones**
```python
import utztime.tz.us
import utztime.tz.ca
```

**To Populate the tzlist registry**
```python
import utztime.tz.us
import utztime.tzlist
utztime.tzlist.registerTimezone(utztime.tz.us.America_Los_Angeles)
utztime.tzlist.registerTimezone(utztime.tz.us.America_Chicago)
utztime.tzlist.registerTimezone(utztime.tz.us.America_Phoenix)
utztime.tzlist.registerTimezone(utztime.tz.us.America_New_York)
```

There is a `EPOCH` const that can be used here if desired.  It is the uPython EPOCH of Jan 1 2000. Not the unix EPOCH of Jan 1 1970.
This EPOCH value is self adjusting to the platforms actual EPOCH
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

**See tz/us.py** for examples.

Not Currently Thread Safe. Uses an internal field state tracked by year.  I'll fix this in the near future.

<a id="utztime.utimezone.TimeChangeRule"></a>

## TimeChangeRule Objects

```python
class TimeChangeRule()
```

Simple data structure to define a change over rule

<a id="utztime.utimezone.TimeChangeRule.__init__"></a>

#### \_\_init\_\_

```python
def __init__(abbrev: str, whichDow: int, dow: int, month: int, hour: int,
             offset: int)
```

abbrev: 5 chars max. eg. DST, EDT, PST...
whichDow: Which day of our dow? see internal FIRST, SECOND, THIRD, etc
dow: day of week, see internal SUN, MON, TUE.. ETC
month: Which Month.  see internal JAN, FEB, MAR.. etc
hour: # 0-23
offset: The timezone offset from UTC in minutes

<a id="utztime.utimezone.TimeChangeRule.clone"></a>

#### clone

```python
def clone() -> 'TimeChangeRule'
```

Create a clone of this rule

<a id="utztime.utimezone.TimeChangeRule.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other) -> bool
```

[==] Operator.  Compares all fields except the abbrev.  Used in the unit test that attempts
    to find re-defined rules.

<a id="utztime.utimezone.TimeChangeRule.__ne__"></a>

#### \_\_ne\_\_

```python
def __ne__(other) -> bool
```

[!=] Operator.

<a id="utztime.utimezone.TimeChangeRule.toTime"></a>

#### toTime

```python
def toTime(yr: int) -> int
```

Convert using this time change rule to a time value
for the given year.

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
def __init__(name: str, std: TimeChangeRule, dst: TimeChangeRule | None)
```

name - name of this timezone.  eg.  America/Chicago
stdStart - The start of Standard Time Rule.
dstStart - Optional. The start of Daylight Savings Time Rule. Set to None if this TZ observes only standard time.

<a id="utztime.utimezone.Timezone.clone"></a>

#### clone

```python
def clone(name: str, shallow: bool = False) -> 'Timezone'
```

Create a complete copy of this timezone.
Provide a new-name for this clone.
shallow will not clone the rules, but instead use the same instance.
This has the benefit of being lighter weight on memory, but running the
risk of side-affects if used incorrectly

<a id="utztime.utimezone.Timezone.link"></a>

#### link

```python
def link(name: str) -> 'Timezone'
```

Shortcut to create a shallow clone

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

[==] Operator. Compares the 2 std & dst rules. Ignores the name differences

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

<a id="utztime.utimezone.Timezone.utcIsSTD"></a>

#### utcIsSTD

```python
def utcIsSTD(utc: int) -> bool
```

Convenient wrapper to utcIsDST

<a id="utztime.utimezone.Timezone.locIsDST"></a>

#### locIsDST

```python
def locIsDST(local: int) -> bool
```

Determine whether the given Local time is within the DST interval
or the Standard time interval.

<a id="utztime.utimezone.Timezone.locIsSTD"></a>

#### locIsSTD

```python
def locIsSTD(utc: int) -> bool
```

Convenient wrapper to locIsDST

<a id="utztime.utzlist"></a>

# utztime.utzlist

A utility class where you can define and store your timezones.
You can use each timezone definition yourself, and store them in your own lists.
Or, you can define and assign them here for a more common interface.
Including the built-in sorting by StandardTime

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

<a id="utztime.utzlist.registerTimezone"></a>

#### registerTimezone

```python
def registerTimezone(tz: tz.Timezone)
```

Set/Add to the internal list of available timezones.
This simply makes the provided timezone accessible
through the getTimezone() function

<a id="utztime.utzlist.clear"></a>

#### clear

```python
def clear()
```

Clear all timezones from the timezone list.
Mostly helpful for unit-testing.

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

month: 1-12

day: 1-31

hour: 0-23

min: 0-59

sec: 0-61

<a id="utztime.tztime.TZTime.isDst"></a>

#### isDst

```python
def isDst() -> bool
```

Return if this time, and the given timezone, is a DST time or not.

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
def toTimezone(tz: utimezone.Timezone | None) -> 'TZTime'
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

<a id="utztime.tz"></a>

# utztime.tz

<a id="utztime.tz.us"></a>

# utztime.tz.us

<a id="utztime.tz.bm"></a>

# utztime.tz.bm

<a id="utztime.tz.ca"></a>

# utztime.tz.ca

