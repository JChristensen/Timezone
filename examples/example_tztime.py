import utztime
import utztime.utzlist

# Simple Example
def zones():

    utcNow = utztime.TZTime()
    estNow = utztime.TZTime(tz=utztime.utzlist.America_Eastern)

    estToUtc = estNow.toUTC()
    utcToEst = utcNow.toTimezone(tz=utztime.utzlist.America_Eastern)

    print(f"EST [{estNow}] to UTC = [{estToUtc}]")
    print(f"UTC [{utcNow}] to EST = [{utcToEst}]")


def mathFuture():

    pstNow = utztime.TZTime(tz=utztime.utzlist.America_Pacific)
    pstFuture = pstNow.plusHours(15).plusMinutes(12).plusSeconds(25)

    print(f"PST [{pstNow}] plus 15h 12m 25s [{pstFuture}]")


def zero():

    cstNow = utztime.TZTime(tz=utztime.utzlist.America_Central)
    cstZero = cstNow.withMinuts(0).withSeconds(0)

    print(f"[{cstNow}] with zero minutes/seconds [{cstZero}]")


if __name__ == '__main__':

    zones()
    mathFuture()
    zero()
