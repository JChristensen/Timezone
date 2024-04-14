# Micropython uTimezone Library
https://github.com/shaneapowell/utimezone

A fork/port of
https://github.com/JChristensen/Timezone

README file
Shane Powell
July 2022

## License
Micropython Timezone Library Copyright (C) 2022 Shane Powell GNU GPL v3.0

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License v3.0 as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/gpl.html>

## Introduction
The **utztime** library is designed to work in conjunction with the [python time or utime package], which must also be installed on your system. This documentation assumes some familiarity with the time library.

The primary aim of the **utztime** library is to convert Universal Coordinated Time (UTC) to the correct local time, whether it is daylight saving time (a.k.a. summer time) or standard time. The time source could be a GPS receiver, an NTP server, or a Real-Time Clock (RTC) set to UTC.  But whether a hardware RTC or other time source is even present is immaterial, since the Time library can function as a software RTC without additional hardware (although its accuracy is dependent on the accuracy of the microcontroller's system clock.)

The **utztime** library implements two objects to facilitate time zone conversions:
- A **TimeChangeRule** object describes when local time changes to daylight (summer) time, or to standard time, for a particular locale.
- A **Timezone** object uses **TimeChangeRule**s to perform conversions and related functions.

## Installation
### MIP
Install `utztime` with [mpremote](https://docs.micropython.org/en/latest/reference/packages.html#installing-packages-with-mpremote) into `/lib/utztime` on the device.
```sh
$ mpremote mip install github:shaneapowell/utimezone/utztime
```

### Manually
copy the entire `tztime` folder from this repo into your python path.

## Examples
see the **examples** folder.

## Coding TimeChangeRules
Normally these will be coded in pairs for a given time zone: One rule to describe when daylight (summer) time starts, and one to describe when standard time starts.

As an example, here in the Eastern US time zone, Eastern Daylight Time (EDT) starts on the 2nd Sunday in March at 02:00 local time. Eastern Standard Time (EST) starts on the 1st Sunday in November at 02:00 local time.

Define a **TimeChangeRule** as follows:

`myRule = TimeChangeRule(abbrev, week, dow, month, hour, offset)`

Where:

**abbrev** is a character string abbreviation for the time zone; Keep it short.

**week** is the week of the month that the rule starts.

**dow** is the day of the week that the rule starts.

**hour** is the hour in local time that the rule starts (0-23).

**offset** is the UTC offset _in minutes_ for the time zone being defined.

For convenience, the following symbolic names can be used:

**week:** FIRST, SECOND, THIRD, FOURTH, LAST
**dow:** SUN, MON, TUE, WED, THU, FRI, SAT
**month:** JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC

For the Eastern US time zone, the **TimeChangeRule**s could be defined as follows:

```python
usEST = TimeChangeRule("EST", utimezone.FIRST, utimezone.SN, utimezone.NOV, 2, -300)    #UTC - 5 hours
usEDT = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)  #UTC - 4 hours
```

## Coding Timezone objects
There are three ways to define **Timezone** objects.

By first defining **TimeChangeRule**s (as above) and giving the daylight time rule and the standard time rule (assuming usEST and usEDT defined as above):
`usEastern = Timezone(usEST, usEDT);`

For a time zone that does not change to daylight/summer time, pass a single rule to the constructor. For example:
`usAZ = Timezone(usMST, usMST);`

## Timezone library methods
Note that the `time` data type is defined by the Python time or utime package.  See the Time package documentation [time](https://docs.python.org/3/library/time.html) and [utime](https://docs.micropython.org/en/v1.15/library/utime.html) for additional details.

### int toLocal(utc: int);
##### Description
Converts the given UTC time to local time, standard or daylight as appropriate.
##### Syntax
`myTZ.toLocal(utc)`
##### Parameters
***utc:*** Universal Coordinated Time *(int)*
##### Returns
Local time *(int)*
##### Example
```python
import utimezone as tz
import time
eastern: int
utc: int
usEDT = TimeChangeRule("EDT", tz.SECOND, tz.SUN, tz.MAR, 2, -240)
usEST = TimeChangeRule("EST", tz.FIRST, tz.SUN, tz.NOV, 2, -300)
usEastern = Timezone(usEST, usEDT)
utc = time.time();	 # current time
eastern = usEastern.toLocal(utc)
```

### bool utcIsDST(utc: int);
### bool locIsDST(local: int);
##### Description
These functions determine whether a given UTC time or a given local time is within the daylight saving (summer) time interval, and return true or false accordingly.
##### Syntax
`utcIsDST(utc);`
`locIsDST(local);`
##### Parameters
***utc:*** Universal Coordinated Time *(int)*
***local:*** Local Time *(int)*
##### Returns
true or false *(bool)*
##### Example
`if (usEastern.utcIsDST(utc)): }`


### setRules(stdStart: TimeChangeRule, dstStart: TimeChangeRule)
##### Description
This function reads or updates the daylight and standard time rules from RAM. Can be used to change TimeChangeRules dynamically while a sketch runs.
##### Syntax
`myTZ.setRules(stdStart, dstStart);`
##### Parameters
***dstStart:*** A TimeChangeRule denoting the start of daylight saving (summer) time.
***stdStart:*** A TimeChangeRule denoting the start of standard time.
##### Returns
None.
##### Example
```python
EDT = TimeChangeRule("EDT", Second, Sun, Mar, 2, -240)
EST = TimeChangeRule("EST", First, Sun, Nov, 2, -300)
CDT = TimeChangeRule("CDT", Second, Sun, Mar, 2, -300)
CST = TimeChangeRule("CST", First, Sun, Nov, 2, -360)
tz = Timezone(CST, DST)
...
tz.setRules(EST, EDT)

```
### int toUTC(local: INT);
##### Description
Converts the given local time to UTC time.

**WARNING:** This function is provided for completeness, but should seldom be needed and should be used sparingly and carefully.

Ambiguous situations occur after the Standard-to-DST and the DST-to-Standard time transitions. When changing to DST, there is one hour of local time that does not exist, since the clock moves forward one hour. Similarly, when changing to standard time, there is one hour of local time that occurs twice since the clock moves back one hour.

This function does not test whether it is passed an erroneous time value during the Local-to-DST transition that does not exist. If passed such a time, an incorrect UTC time value will be returned.

If passed a local time value during the DST-to-Local transition that occurs twice, it will be treated as the earlier time, i.e. the time that occurs before the transition.

Calling this function with local times during a transition interval should be avoided!
##### Syntax
`myTZ.toUTC(local)`
##### Parameters
***local:*** Local Time *(int)*
##### Returns
UTC *(int)*
