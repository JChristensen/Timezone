# Micropython uTime/TimeZone Library
[![tests](https://github.com/shaneapowell/utimezone/actions/workflows/tests.yml/badge.svg)](https://github.com/shaneapowell/utimezone/actions/workflows/tests.yml)

https://github.com/shaneapowell/utimezone


A fork/port of (and more)
https://github.com/JChristensen/Timezone


# License
Micropython Timezone Library Copyright (C) 2022 Shane Powell GNU GPL v3.0

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License v3.0 as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/gpl.html>

# Introduction
The **utztime** library is designed to work in conjunction with the [python time or utime package], which must also be installed on your system. This documentation assumes some familiarity with the time library.

The primary aim of the **utztime** library is to convert Universal Coordinated Time (UTC) to the correct local time, whether it is daylight saving time (a.k.a. summer time) or standard time. The time source could be a GPS receiver, an NTP server, or a Real-Time Clock (RTC) set to UTC.  But whether a hardware RTC or other time source is even present is immaterial, since the Time library can function as a software RTC without additional hardware (although its accuracy is dependent on the accuracy of the microcontroller's system clock.)

The **utztime** library is made up of 4 primary parts.
- A **TimeChangeRule** object describes when local time changes to daylight (summer) time, or to standard time, for a particular locale.
- A **Timezone** object uses **TimeChangeRule**s to perform conversions and related functions.
- A **TZTime** Object to handle and manipulate time, avoiding the direct use of the standard `time` lib.
- A **utzlist** Object with some pre-defined American TimeZone definitions.

# Limitation
- Epoch!  This library relies on the system `time` library.  Due to that fact, calculating timezone specific values before teh system Epoch (2000 for upy, 1970 for unix) fails.

# Installation
## MIP
Install `utztime` with [mpremote](https://docs.micropython.org/en/latest/reference/packages.html#installing-packages-with-mpremote) into `/lib/utztime` on the device.
```sh
mpremote mip install github:shaneapowell/utimezone
```

## MIP (.py)
You can optionally install the non .mpy original source
```sh
mpremote mip install github:shaneapowell/utimezone/package-raw.json
```

## Manually
- Make sure you have a python3 runtime installed.  3.8 -> 3.12 currently supported.
- Clone this repo
    ```
    git clone https://github.com/shaneapowell/utimezone.git
    ```
- Install `pipenv` tool on your computer
  ```
  pip3 install pipenv
  ```
- Create the local venv (only needed once)
  ```
  pipenv sync
  ```
- Build the .mpy files
  ```
  pipenv run build
  ```
- Plug your micropython device into your computer.
- Deploy the library
  this command assumes your device appears as `/dev/ttyACM0`.
  ```
  pipenv run deploy /dev/ttyACM0
  ```
- Try it out
  ```
  pipenv run example
  ```


# Examples
see the [**examples**](examples) folder.

# API Documentation
Read the [API Docs](docs/API.md)

# Unit Tests
You can run the suite of unit tests on your micropython board, or a unix micropython emulator.
## Local python
```sh
pipenv run tests
```
## On a device
```sh
pipenv run utests /dev/ttyACM0
```
## On an Emulator
You'll need the `micropython` binary installed on your system.
```sh
pipenv run etests
```

# Adding New TimeZones to this Library.
I'm more than happy to accept PullRequests to add new TimeZone definitions.
I'm Canadian Born, living in USA. So it's no surprise I started with the time zones I'm familiar with.
Just follow these guidelines in creating a new TimeZone definition.

Reference the standard TimeZone identifier names to figure out what directory, and filename(s) you'll be creating.
[https://en.wikipedia.org/wiki/List_of_tz_database_time_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

TimeZones in this library are grouped by country.  They are stored in a single file per country, using the country code abbreviation.
Look in `/src/utztime/tz` for the current definition files.  `us.py` contains all USA timezone definitions.  `ca.py` for all Canadian definitions.
The reason for keeping the definitions within separate country code files, is to streamline the memory overhead.  Instead of having your program import
every possible definition, which will use up a good deal of memory, you can reference them in smaller chunks.

In an effort to streamline memory constraints even more, there is the concept of linking a timezone to an existing full definition.
This saves on a small amount of ram, by re-using the existing rule definition in the original timezone, and only really adding a name string.
see `/src/utztime/tz/ca.py` for some examples of this.

To create a brand new definition file, please reference `us.py` as an example of how to structure your new file.
Defining a list of any new `Rules` at the top, then each `Timezone` definition referencing these rules.  Then any `linked` timezones.

Be careful overusing existing rules and zones in linked zones.  This can lead to a cascading increase in the used memory footprint.
The `ca.py` file references the `us.py` file for most of it's zones, as all but 2 are linked.  This is not too inefficient.
However, the `bm.py` file references the `ca.py`, which itself references the `us.py` file, just for a single pair of `rules`.  This can be risky if not careful.

Finally, create a unit-test for the new zone file, or add to the existing one.
You only need to test zones that are not canonical zones (not linked).
see `/tests/test_tz_us.py` and `/tests/test_tz_ca.py` for examples. There is a basic utility test function created that does the
rudimentary testing needed for each defined zone.

If you have created a new `test_tz_XX.py` file, you must also add it's include to the `/test/__init__.py` file


# Before Submitting a PR
```sh
# Run the linter and typechecker
pipenv run linter
pipenv run typechecker

# Build the .mpy files
pipenv run build

# Run the tests locally. Take note of the number of tests run.  eg.. 50
pipenv run tests

# Run the tests in a local micropython emulator.  Make sure the same number of tests ran as above.
# If the count is off, you might have forgot to add your new test.py file to the `/test/__init__.py` file
pipenv run etests

# Run the tests on a device.
# This could prove challenging on smaller upy devices.
# I happen to have some Xaio esp32S3 devices with 8M of psram on board.
# If this becomes an issue, I'll figure out a simple way to break the tests into segments.
pipenv run deploy /dev/ttyACM0
pipenv run utests /dev/ttyACM0
```
