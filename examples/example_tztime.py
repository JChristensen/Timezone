import utztime
import utztime.utzlist as tzl
from utztime.tz.america.new_york import America_New_York
from utztime.tz.america.chicago import America_Chicago
from utztime.tz.america.phoenix import America_Phoenix
from utztime.tz.america.los_angeles import America_Los_Angeles


# Simple Example
def zones():

    utcNow = utztime.TZTime()
    estNow = utztime.TZTime(America_New_York)

    estToUtc = estNow.toUTC()
    utcToEst = utcNow.toTimezone(tz=utztime.utzlist.America_Eastern)

    print(f"EST [{estNow}] to UTC = [{estToUtc}]")
    print(f"UTC [{utcNow}] to EST = [{utcToEst}]")


def mathFuture():

    pstNow = utztime.TZTime(tz=America_Los_Angeles)
    pstFuture = pstNow.plusHours(15).plusMinutes(12).plusSeconds(25)

    print(f"PST [{pstNow}] plus 15h 12m 25s [{pstFuture}]")


def zero():

    cstNow = utztime.TZTime(tz=America_Chicago)
    cstZero = cstNow.withMinuts(0).withSeconds(0)

    print(f"[{cstNow}] with zero minutes/seconds [{cstZero}]")


if __name__ == '__main__':

    tzl.setTimezone(America_New_York)
    tzl.setTimezone(America_Chicago)
    tzl.setTimezone(America_Los_Angeles)
    tzl.setTimezone(America_Phoenix)

    zones()
    mathFuture()
    zero()
