# Arduino Timezone Library
https://github.com/JChristensen/Timezone  
README file  
Jack Christensen  
Mar 2012  

## License
Arduino Timezone Library Copyright (C) 2018 Jack Christensen GNU GPL v3.0

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License v3.0 as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/gpl.html>

## Introduction
The **Timezone** library is designed to work in conjunction with the [Arduino Time library](https://github.com/PaulStoffregen/Time), which must also be installed on your system. This documentation assumes some familiarity with the Time library.

The primary aim of the **Timezone** library is to convert Universal Coordinated Time (UTC) to the correct local time, whether it is daylight saving time (a.k.a. summer time) or standard time. The time source could be a GPS receiver, an NTP server, or a Real-Time Clock (RTC) set to UTC.  But whether a hardware RTC or other time source is even present is immaterial, since the Time library can function as a software RTC without additional hardware (although its accuracy is dependent on the accuracy of the microcontroller's system clock.)

The **Timezone** library implements two objects to facilitate time zone conversions:
- A **TimeChangeRule** object describes when local time changes to daylight (summer) time, or to standard time, for a particular locale.
- A **Timezone** object uses **TimeChangeRule**s to perform conversions and related functions.  It can also write its **TimeChangeRule**s to EEPROM, or read them from EEPROM.  Multiple time zones can be represented by defining multiple **Timezone** objects.

## Examples
The following example sketches are included with the **Timezone** library:

- **Clock:** A simple self-adjusting clock for a single time zone.  **TimeChangeRule**s may be optionally read from EEPROM.
- **HardwareRTC:** A self-adjusting clock for one time zone using an external real-time clock, either a DS1307 or DS3231 (e.g. Chronodot) which is set to UTC.  
- **WorldClock:** A self-adjusting clock for multiple time zones.
- **WriteRules:** A sketch to write **TimeChangeRule**s to EEPROM.
- **Change_TZ_1:** Changes between time zones by modifying the TimeChangeRules.
- **Change_TZ_2:** Changes between time zones by selecting from an array of Timezone objects.

## Coding TimeChangeRules
Normally these will be coded in pairs for a given time zone: One rule to describe when daylight (summer) time starts, and one to describe when standard time starts.

As an example, here in the Eastern US time zone, Eastern Daylight Time (EDT) starts on the 2nd Sunday in March at 02:00 local time. Eastern Standard Time (EST) starts on the 1st Sunday in November at 02:00 local time.

Define a **TimeChangeRule** as follows:

`TimeChangeRule myRule = {abbrev, week, dow, month, hour, offset};`

Where:

**abbrev** is a character string abbreviation for the time zone; it must be no longer than five characters.

**week** is the week of the month that the rule starts.

**dow** is the day of the week that the rule starts.

**hour** is the hour in local time that the rule starts (0-23).

**offset** is the UTC offset _in minutes_ for the time zone being defined.

For convenience, the following symbolic names can be used:

**week:** First, Second, Third, Fourth, Last  
**dow:** Sun, Mon, Tue, Wed, Thu, Fri, Sat  
**month:** Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec

For the Eastern US time zone, the **TimeChangeRule**s could be defined as follows:

```c++
TimeChangeRule usEDT = {"EDT", Second, Sun, Mar, 2, -240};  //UTC - 4 hours
TimeChangeRule usEST = {"EST", First, Sun, Nov, 2, -300};   //UTC - 5 hours
```
## Special Case TimeChangeRules
A special case exists for certain locales (notably Greenland) where the combination of a "Last" rule and an early change point causes the time change to occur late on the previous day, local time. These cannot be coded as above. Instead, use a negative hour to indicate when the change occurs in the previous day. A -1 would indicate 23:00, -2 would indicate 22:00, etc.

This works as follows for Greenland.
```c++
// West Greenland Summer Time, West Greenland Time (e.g. Nuuk)
TimeChangeRule wgst = {"WGST", Last, Sun, Mar, -1, -60};   // UTC-1 hour
TimeChangeRule wgt  = {"WGT", Last, Sun, Oct, 0, -120};    // UTC-2 hours
```
WGST is defined as beginning on the last Sunday in March at 01:00 UTC, or 23:00 Saturday WGT. For 2026, the change would happen as follows:
```
Sat Mar 28 22:59:58 2026 WGT
Sat Mar 28 22:59:59 2026 WGT
Sun Mar 29 00:00:00 2026 WGST
Sun Mar 29 00:00:01 2026 WGST
```
Compare the output of the [Greenland example sketch](https://github.com/JChristensen/Timezone/blob/master/examples/Greenland/Greenland.ino) with the [tz database dump](https://github.com/JChristensen/Timezone/blob/master/examples/zdump-greenland.txt).

## Coding Timezone objects
There are three ways to define **Timezone** objects.

By first defining **TimeChangeRule**s (as above) and giving the daylight time rule and the standard time rule (assuming usEDT and usEST defined as above):  
`Timezone usEastern(usEDT, usEST);`

For a time zone that does not change to daylight/summer time, pass a single rule to the constructor. For example:  
`Timezone usAZ(usMST, usMST);`

By reading rules previously stored in EEPROM.  This reads both the daylight and standard time rules previously stored at EEPROM address 100:  
`Timezone usPacific(100);`

Note that **TimeChangeRule**s require 12 bytes of storage each, so the pair of rules associated with a Timezone object requires 24 bytes total.  This could possibly change in future versions of the library.  The size of a **TimeChangeRule** can be checked with `sizeof(usEDT)`.

## Timezone library methods
Note that the `time_t` data type is defined by the Arduino Time library, TimeLib.h. See the Time library documentation [here](https://www.pjrc.com/teensy/td_libs_Time.html) and [here](https://github.com/PaulStoffregen/Time) for additional details.

### time_t toLocal(time_t utc);
##### Description
Converts the given UTC time to local time, standard or daylight as appropriate.
##### Syntax
`myTZ.toLocal(utc);`
##### Parameters
***utc:*** Universal Coordinated Time *(time_t)*  
##### Returns 
Local time *(time_t)*  
##### Example
```c++
time_t eastern, utc;
TimeChangeRule usEDT = {"EDT", Second, Sun, Mar, 2, -240};  //UTC - 4 hours
TimeChangeRule usEST = {"EST", First, Sun, Nov, 2, -300};   //UTC - 5 hours
Timezone usEastern(usEDT, usEST);
utc = now();	//current time from the Time Library
eastern = usEastern.toLocal(utc);
```

### time_t toLocal(time_t utc, TimeChangeRule **tcr);
##### Description
As above, converts the given UTC time to local time, and also returns a pointer to the **TimeChangeRule** that was applied to do the conversion. This could then be used, for example, to include the time zone abbreviation as part of a time display.  The caller must take care not to alter the pointed **TimeChangeRule**, as this will then result in incorrect conversions.
##### Syntax
`myTZ.toLocal(utc, &tcr);`  
##### Parameters
***utc:*** Universal Coordinated Time *(time_t)*  
***tcr:*** Address of a pointer to a **TimeChangeRule** _(\*\*TimeChangeRule)_   
##### Returns
Local time *(time_t)*  
Pointer to **TimeChangeRule**  _(\*\*TimeChangeRule)_    
##### Example
```c++
time_t eastern, utc;
TimeChangeRule *tcr;
TimeChangeRule usEDT = {"EDT", Second, Sun, Mar, 2, -240};  //UTC - 4 hours
TimeChangeRule usEST = {"EST", First, Sun, Nov, 2, -300};   //UTC - 5 hours
Timezone usEastern(usEDT, usEST);
utc = now();	//current time from the Time Library
eastern = usEastern.toLocal(utc, &tcr);
Serial.print("The time zone is: ");
Serial.println(tcr -> abbrev);
```

### bool utcIsDST(time_t utc);
### bool locIsDST(time_t local);
##### Description
These functions determine whether a given UTC time or a given local time is within the daylight saving (summer) time interval, and return true or false accordingly.
##### Syntax
`utcIsDST(utc);`  
`locIsDST(local);`  
##### Parameters
***utc:*** Universal Coordinated Time *(time_t)*  
***local:*** Local Time *(time_t)*  
##### Returns
true or false *(bool)*
##### Example
`if (usEastern.utcIsDST(utc)) { /*do something*/ }`

### void readRules(int address);
### void writeRules(int address);
##### Description
These functions read or write a **Timezone** object's two **TimeChangeRule**s from or to EEPROM.
##### Syntax
`myTZ.readRules(address);`  
`myTZ.writeRules(address);`  
##### Parameters
***address:*** The beginning EEPROM address to write to or read from *(int)*
##### Returns
None.
##### Example
`usEastern.writeRules(100);  //write rules beginning at EEPROM address 100`

### void setRules(TimeChangeRule dstStart, TimeChangeRule stdStart);
##### Description
This function reads or updates the daylight and standard time rules from RAM. Can be used to change TimeChangeRules dynamically while a sketch runs.
##### Syntax
`myTZ.setRules(dstStart, stdStart);`  
##### Parameters
***dstStart:*** A TimeChangeRule denoting the start of daylight saving (summer) time.  
***stdStart:*** A TimeChangeRule denoting the start of standard time.
##### Returns
None.
##### Example
```c++
TimeChangeRule EDT = {"EDT", Second, Sun, Mar, 2, -240};
TimeChangeRule EST = {"EST", First, Sun, Nov, 2, -300};
Timezone ET(EDT, EST);
...
tz.setRules(EDT, EST);

```
### time_t toUTC(time_t local);
##### Description
Converts the given local time to UTC time.

**WARNING:** This function is provided for completeness, but should seldom be needed and should be used sparingly and carefully.

Ambiguous situations occur after the Standard-to-DST and the DST-to-Standard time transitions. When changing to DST, there is one hour of local time that does not exist, since the clock moves forward one hour. Similarly, when changing to standard time, there is one hour of local time that occurs twice since the clock moves back one hour.

This function does not test whether it is passed an erroneous time value during the Local-to-DST transition that does not exist. If passed such a time, an incorrect UTC time value will be returned.

If passed a local time value during the DST-to-Local transition that occurs twice, it will be treated as the earlier time, i.e. the time that occurs before the transition.

Calling this function with local times during a transition interval should be avoided!
##### Syntax
`myTZ.toUTC(local);`
##### Parameters
***local:*** Local Time *(time_t)*  
##### Returns
UTC *(time_t)*  
