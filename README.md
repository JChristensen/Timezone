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
I'm Canadian Born, living in USA. So, no surprise I started with the time zones I'm familiar with.
Just follow these guidelines in creating a new TimeZone definition.

Reference the standard TimeZone identifier names to figure out what directory, and filename(s) you'll be creating.

[https://en.wikipedia.org/wiki/List_of_tz_database_time_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

Simply find the time zone (or zones) by the `TZ Identifier` in this list.

## File Name
The name of your timezone definition(s) file must be lowercase, and should be placed in a directory/file pattern similar to the onces already added.
see `tz/america/phoenix` as an example.  It is a good example as it happens to contain 3 definitions in one file.

If you wish to add a timezone with the standard TZ identifier of `