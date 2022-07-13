import utimezone as tz
from utimezone import TimeChangeRule, Timezone
import time
import ntptime
from machine import RTC

# Simple Example
def simple():
    edt = TimeChangeRule("EDT", tz.SECOND, tz.SUN, tz.MAR, 2, -240)
    est = TimeChangeRule("EST", tz.FIRST,  tz.SUN, tz.NOV, 2, -300)

    tz = Timezone(est, edt)

    utc = time.time()
    loc = tz.toLocal(utc)

    print(time.gmtime(utc))
    print(time.gmtime(loc))



# Change TZ
def changeTz():

    edt = TimeChangeRule("EDT", tz.SECOND, tz.SUN, tz.MAR, 2, -240)
    est = TimeChangeRule("EST", tz.FIRST,  tz.SUN, tz.NOV, 2, -300)
    cdt = TimeChangeRule("CDT", tz.SECOND, tz.SUN, tz.MAR, 2, -300)
    cst = TimeChangeRule("CST", tz.FIRST,  tz.SUN, tz.NOV, 2, -360)

    tz = Timezone(est, edt)
    utc = time.time()
    loc = tz.toLocal(utc)
    print(time.gmtime(loc))

    tz.setRules(cst, cdt)
    loc = tz.toLocal(utc)
    print(time.gmtime(loc))


