/*----------------------------------------------------------------------*
 * Timezone library example sketch.                                     *
 * Write TimeChangeRules to EEPROM.                                     *
 * Jack Christensen Mar 2012                                            *
 *                                                                      *
 * CC BY-SA 4.0: This work is licensed under the Creative Commons       *
 * Attribution-ShareAlike 4.0 International License,                    *
 * https://creativecommons.org/licenses/by-sa/4.0/                      *
 *----------------------------------------------------------------------*/

#include <Timezone.h>    // https://github.com/JChristensen/Timezone

// US Eastern Time Zone (New York, Detroit)
TimeChangeRule usEdt = {"EDT", Second, Sun, Mar, 2, -240};    // UTC - 4 hours
TimeChangeRule usEst = {"EST", First, Sun, Nov, 2, -300};     // UTC - 5 hours
Timezone usEastern(usEdt, usEst);

void setup(void)
{
    pinMode(13, OUTPUT);
    usEastern.writeRules(100);    // write rules to EEPROM address 100
}

void loop(void)
{
    // fast blink to indicate EEPROM write is complete
    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);
}

