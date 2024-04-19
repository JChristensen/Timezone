import sys

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