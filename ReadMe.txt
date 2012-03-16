ReadMe file for Arduino Timezone Library v1.0
https://github.com/JChristensen/Timezone
Jack Christensen Mar 2012

This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
Unported License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to Creative
Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.

--------------------------------------------------------------------------------
This library is designed to work in conjunction with the Arduino Time library at
http://www.arduino.cc/playground/Code/Time. The Time library must be referenced
in your sketch with #include <Time.h>. This documentation assumes some
familiarity with the Time library.

A primary aim of this library is to allow a Real Time Clock (RTC) to be set to
Universal Coordinated Time (UTC) and then convert the UTC time to the correct
local time, whether it is daylight saving time (a.k.a. summer time) or standard
time. Whether a hardware RTC is present or not is immaterial; the Time library
will function as a software RTC without additional hardware, although software
RTC accuracy will be determined by the accuracy of the microcontroller's system
clock.

The Timezone library implements two objects to facilitate time zone conversions:

(1) A "TimeChangeRule" object describes when local time changes to daylight
(summer) time, or to standard time, for a particular locale.

(2) A "Timezone" object performs conversions and related functions. It can also
write its TimeChangeRules to EEPROM, or read them from EEPROM. Multiple time
zones can be represented by declaring multiple Timezone objects.

To use the library:
(1) Go to https://github.com/JChristensen/Timezone/downloads and download the
file in the compressed format of your choice (zip or tar.gz) to a convenient
location on your PC.
(2) Uncompress the downloaded file. This will result in a folder containing all
the files for the library, that has a name similar to "JChristensen-
Timezone-42e98a7".
(3) Rename the folder to just "Timezone".
(4) Copy the renamed folder to the Arduino sketchbook\libraries folder.

--------------------------------------------------------------------------------
The following example sketches are included with the Timezone library:

Clock: A simple self-adjusting clock for a single time zone.
TimeChangeRules may be optionally read from EEPROM.

WorldClock: A self-adjusting clock for multiple time zones.

WriteRules: A sketch to write TimeChangeRules to EEPROM.

--------------------------------------------------------------------------------
Coding TimeChangeRules:

Normally these will be coded in pairs for a given time zone: One rule to
describe when daylight (summer) time starts, and one to describe when standard
time starts.

As an example, here in the Eastern US time zone, Eastern Daylight Time (EDT)
starts on the 2nd Sunday in March at 02:00 local time. Eastern Standard Time
(EST) starts on the 1st Sunday in November at 02:00 local time.

Declare a TimeChangeRule as follows:

TimeChangeRule myRule = {abbrev, week, dow, month, hour, offset};

Where:

abbrev  is a character string abbreviation for the time zone,
        it must be no longer than five characters.

week    is the week of the month that the rule starts.

dow     is the day of the week that the rule starts.

hour    is the hour in local time that the rule starts.

offset  is the UTC offset IN MINUTES for the time zone being defined.

For convenience, the following symbolic names can be used:

week:   First, Second, Third, Fourth, Last
dow:    Sun, Mon, Tue, Wed, Thu, Fri, Sat
month:  Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec

So for the Eastern US time zone, the time change rules could be defined as
follows:

TimeChangeRule usEDT = {"EDT", Second, Sun, Mar, 2, -240};  //UTC - 4 hours
TimeChangeRule usEST = {"EST", First, Sun, Nov, 2, -300};   //UTC - 5 hours

For a time zone that does not change to daylight/summer time, simply code two
identical rules, only the offset is important, choose any valid value for week,
dow, month and hour.

--------------------------------------------------------------------------------
Declaring Timezone objects

There are two ways to declare Timezone objects.

(1) By first defining TimeChangeRules (as above) and giving the daylight time
rule and the standard time rule (assuming usEDT and usEST defined as above):

    Timezone usEastern(usEDT, usEST);

(2) By reading rules previously stored in EEPROM. This reads both the daylight
and standard time rules previously stored at EEPROM address 100:

    Timezone usPacific(100);

Note that TimeChangeRules require 12 bytes of storage each, so the pair of
rules associated with a Timezone object require 24 bytes total. This could
possibly change in future versions of the library. The size of a TimeChangeRule
can be checked via sizeof(), e.g.: sizeof(usEDT).

--------------------------------------------------------------------------------
Timezone functions

Note that the time_t type is defined by the Time library <Time.h>. See the Time
library documentation for additional details.

time_t toLocal(time_t utc);
Converts the given UTC time to local time, standard or daylight as appropriate.
Example:
    time_t eastern, utc;
    TimeChangeRule usEDT = {"EDT", Second, Sun, Mar, 2, -240};  //UTC - 4 hours
    TimeChangeRule usEST = {"EST", First, Sun, Nov, 2, -300};   //UTC - 5 hours
    Timezone usEastern(usEDT, usEST);
    utc = now();
    eastern = usEastern.toLocal(utc);

time_t toLocal(time_t utc, TimeChangeRule **tcr);
Converts the given UTC time to local time, as above, and also returns a pointer
to the TimeChangeRule that was applied to do the conversion. This could then be
used, for example, to include the time zone abbreviation as part of a time
display. The caller must take care not to alter the pointed TimeChangeRule, as
this will then result in incorrect conversions.
Example:
    time_t eastern, utc;
    TimeChangeRule *tcr;
    TimeChangeRule usEDT = {"EDT", Second, Sun, Mar, 2, -240};  //UTC - 4 hours
    TimeChangeRule usEST = {"EST", First, Sun, Nov, 2, -300};   //UTC - 5 hours
    Timezone usEastern(usEDT, usEST);
    utc = now();
    eastern = usEastern.toLocal(utc, &tcr);
    Serial.print("The time zone is: ");
    Serial.println(tcr -> abbrev);

boolean utcIsDST(time_t utc);
boolean locIsDST(time_t local);
These functions determine whether the given UTC time or the given local time is
within the daylight saving (summer) time interval, and return true or false
accordingly.
Example:
    if (usEastern.utcIsDst(utc)) {/*do something*/}

void readRules(int address);
void writeRules(int address);
These functions read or write a Timezone object's two TimeChangeRules from or to
EEPROM.
Example:
    usEastern.writeRules(100);  //write rules beginning at EEPROM address 100

time_t toUTC(time_t local);
Converts the given local time to UTC time.
WARNING: This function is provided for completeness, but should seldom be needed
and should be used sparingly and carefully.

Ambiguous situations occur after the Standard-to-DST and the DST-to-Standard
time transitions. When changing to DST, there is one hour of local time that
does not exist, since the clock moves forward one hour. Similarly, when changing
to standard time, there is one hour of local times that occur twice since the
clock moves back one hour.

This function does not test whether it is passed an erroneous time value during
the Local-to-DST transition that does not exist. If passed such a time, an
incorrect UTC time value will be returned.

If passed a local time value during the DST-to-Local transition that occurs
twice, it will be treated as the earlier time, i.e. the time that occurs before
the transistion.

Calling this function with local times during a transition interval should be
avoided!
--------------------------------------------------------------------------------
