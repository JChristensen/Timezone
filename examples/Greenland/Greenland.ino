// Arduino Timezone Library Copyright (C) 2025 by Jack Christensen and
// licensed under GNU GPL v3.0, https://www.gnu.org/licenses/gpl.html
//
// Arduino Timezone Library example sketch.
// Sketch to test DST changes for Greenland.
// Jack Christensen 27Oct2025

#include <Timezone.h>   // https://github.com/JChristensen/Timezone
#include <TimeLib.h>    // https://github.com/PaulStoffregen/Time

// West Greenland Summer Time, West Greenland Time (e.g. Nuuk)
TimeChangeRule wgst = {"WGST", Last, Sun, Mar, -1, -60};   // UTC-1 hour
TimeChangeRule wgt  = {"WGT", Last, Sun, Oct, 0, -120};    // UTC-2 hours
Timezone wg{wgst, wgt};

// US Eastern Daylight Time, Eastern Standard Time (e.g. New York, Detroit)
TimeChangeRule edt = {"EDT", Second, Sun, Mar, 2, -240};  // UTC-4 hours
TimeChangeRule est = {"EST", First, Sun, Nov, 2, -300};   // UTC-5 hours
Timezone et{edt, est};

void setup()
{
    Serial.begin(115200);

    // Greenland
    printTimes(31,  3, 2024, wgst.hour,  wgt.offset, wg);   // day, month, year, hour, offset, tz
    printTimes(27, 10, 2024,  wgt.hour, wgst.offset, wg);
    printTimes(30,  3, 2025, wgst.hour,  wgt.offset, wg);
    printTimes(26, 10, 2025,  wgt.hour, wgst.offset, wg);
    printTimes(29,  3, 2026, wgst.hour,  wgt.offset, wg);
    printTimes(25, 10, 2026,  wgt.hour, wgst.offset, wg);
    printTimes(28,  3, 2027, wgst.hour,  wgt.offset, wg);
    printTimes(31, 10, 2027,  wgt.hour, wgst.offset, wg);
    printTimes(26,  3, 2028, wgst.hour,  wgt.offset, wg);
    printTimes(29, 10, 2028,  wgt.hour, wgst.offset, wg);
    printTimes(25,  3, 2029, wgst.hour,  wgt.offset, wg);
    printTimes(28, 10, 2029,  wgt.hour, wgst.offset, wg);
    printTimes(31,  3, 2030, wgst.hour,  wgt.offset, wg);
    printTimes(27, 10, 2030,  wgt.hour, wgst.offset, wg);

    // US Eastern
    printTimes(10,  3, 2024, edt.hour, est.offset, et);     // day, month, year, hour, offset, tz
    printTimes( 3, 11, 2024, est.hour, edt.offset, et);
    printTimes( 9,  3, 2025, edt.hour, est.offset, et);
    printTimes( 2, 11, 2025, est.hour, edt.offset, et);
    printTimes( 8,  3, 2026, edt.hour, est.offset, et);
    printTimes( 1, 11, 2026, est.hour, edt.offset, et);
    printTimes(14,  3, 2027, edt.hour, est.offset, et);
    printTimes( 7, 11, 2027, est.hour, edt.offset, et);
    printTimes(12,  3, 2028, edt.hour, est.offset, et);
    printTimes( 5, 11, 2028, est.hour, edt.offset, et);
    printTimes(11,  3, 2029, edt.hour, est.offset, et);
    printTimes( 4, 11, 2029, est.hour, edt.offset, et);
    printTimes(10,  3, 2030, edt.hour, est.offset, et);
    printTimes( 3, 11, 2030, est.hour, edt.offset, et);
}

void loop() {}

// print corresponding UTC and local times "n" seconds before and after the time change.
// h is the hour to change the clock using the *current* time (i.e. before the change).
// offset is the utc offset in minutes for the time *after* the change.
void printTimes(int8_t d, int8_t m, int y, int8_t h, int offset, Timezone tz)
{
    const time_t n{2};  // number of seconds to print before and after the time change
    tmElements_t tm;
    tm.Hour = 0;
    tm.Minute = 0;
    tm.Second = 0;
    tm.Day = d;
    tm.Month = m;
    tm.Year = y - 1970; // offset from 1970
    time_t utc = makeTime(tm) - (offset * SECS_PER_MIN) + (h * SECS_PER_HOUR) - n;
    
    Serial.print(F("\n-------- "));
    Serial.print(monthShortStr(m));
    Serial.print('-');
    Serial.print(y);
    Serial.print(F(" time change --------\n"));

    for (uint16_t i=0; i<n*2; i++) {
        TimeChangeRule* tcr;    // pointer to the time change rule, use to get TZ abbrev
        time_t local = tz.toLocal(utc, &tcr);
        printDateTime(utc, "UT = ");
        printDateTime(local, tcr -> abbrev);
        Serial.println();
        ++utc;
    }
}

// format and print a time_t value, with a time zone appended.
void printDateTime(time_t t, const char *tz)
{
    char buf[32];
    char m[4];    // temporary storage for month string (DateStrings.cpp uses shared buffer)
    strcpy(m, monthShortStr(month(t)));
    sprintf(buf, "%s %s %2d %.2d:%.2d:%.2d %d %s",
        dayShortStr(weekday(t)), m, day(t), hour(t), minute(t), second(t), year(t), tz);
    Serial.print(buf);
}
