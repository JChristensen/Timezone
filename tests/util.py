import sys
from utztime.tztime import TZTime
from utztime.utimezone import Timezone

# upython and unix python, use 2 different EPOCHs
UPYTHON_EPOCH = 946706400  # (2000, 1, 1, 0, 0, 0)


def unixToUpyTime(t: int) -> int:
    """
    Given the different Epoch values between unix and a real device.
    This convenient function automatically adjusts the
    time provided in UNIX time, to 2000 Epich Micropython Time.
    eg... 1657745923 becomes 711039523
    """
    if sys.implementation.name == "micropython" and "linux" not in sys.implementation._machine:
        return t - UPYTHON_EPOCH
    else:
        return t


def testStdAndDst(stdTime: TZTime, dstTime: TZTime, tz: Timezone, expectStd: bool = True, expectDst: bool = True):
    """
    Take a pair of time values known to be within standard time, and daylight savings time, for the
    given timezone, and verify the TimeZone correctly detects the STD/DST
    """
    assert stdTime.tz() is None, "Must provide a stdTime without an assigned timezone."
    assert dstTime.tz() is None, "Must provide a dstTime without an assigned timezone."

    assert stdTime.isSTD() is True
    assert stdTime.isDST() is False
    assert dstTime.isSTD() is True
    assert dstTime.isDST() is False

    stdTime = stdTime.withTimezone(tz)
    dstTime = dstTime.withTimezone(tz)

    assert stdTime.isSTD() is expectStd
    assert stdTime.isDST() is not expectStd
    assert dstTime.isDST() is expectDst
    assert dstTime.isSTD() is not expectDst

