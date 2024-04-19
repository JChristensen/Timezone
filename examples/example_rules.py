from utztime import utimezone
from utztime.utimezone import TimeChangeRule, Timezone
import time

# Simple Example
def simple():
    edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    est = TimeChangeRule("EST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -300)

    tz = Timezone(est, edt)

    utc = time.time()
    loc = tz.toLocal(utc)

    print(time.gmtime(utc))
    print(time.gmtime(loc))



# Change TZ
def changeTz():

    edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    est = TimeChangeRule("EST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -300)
    cdt = TimeChangeRule("CDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -300)
    cst = TimeChangeRule("CST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -360)

    tz = Timezone(est, edt)
    utc = time.time()
    loc = tz.toLocal(utc)
    print(time.gmtime(loc))

    tz._setRules(cst, cdt)
    loc = tz.toLocal(utc)
    print(time.gmtime(loc))



if __name__ == '__main__':

    simple()
    changeTz()