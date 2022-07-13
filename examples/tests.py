import utimezone
from utimezone import TimeChangeRule, Timezone
import time
"""
Simple manual test than can easily be run on a micropython board.
ampy --port /dev/ttyUSB0 run examples/tests.py
"""

OK = "OK"
FAIL = "FAIL"

# UTC within EDT
UTC_01 =  711043123  # (2022, 7, 13, 15, 58, 43, 194)
EAST_01 = 711028723  # (2022, 7, 13, 11, 58, 43, 194)
CENT_01 = 711025123  # (2022, 7, 13, 10, 58, 43, 194)

# UTC within EST
UTC_02 =  695404723  # (2022, 1, 13, 15, 58, 43, 194)
EAST_02 = 695386723  # (2022, 1, 13, 10, 58, 43, 194)
CENT_02 = 695383123  # (2022, 1, 13, 9, 58, 43, 194)


def test_utc_to_edt():

    print("\ntest_utc_to_edt")

    # Given
    edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    est = TimeChangeRule("EST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -300)
    tz = Timezone(est, edt)

    # When
    loc = tz.toLocal(UTC_01)

    # Then
    print(f"{UTC_01} -> {EAST_01} == {loc} --> ", end="")
    if loc == EAST_01:
        print(OK)
    else:
        print(FAIL)


def test_utc_to_est():

    print("\ntest_utc_to_est")

    # Given
    edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    est = TimeChangeRule("EST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -300)
    tz = Timezone(est, edt)

    # When
    loc = tz.toLocal(UTC_02)

    # Then
    print(f"{UTC_02} -> {EAST_02} == {loc} --> ", end="")
    if loc == EAST_02:
        print(OK)
    else:
        print(FAIL)



def test_edt_to_utc():

    print("\ntest_edt_to_utc")

    # Given
    edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    est = TimeChangeRule("EST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -300)
    tz = Timezone(est, edt)

    # When
    utc = tz.toUTC(EAST_01)

    # Then
    print(f"{EAST_01} -> {UTC_01} == {utc} --> ", end="")
    if utc == UTC_01:
        print(OK)
    else:
        print(FAIL)


def test_est_to_utc():

    print("\ntest_est_to_utc")

    # Given
    edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    est = TimeChangeRule("EST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -300)
    tz = Timezone(est, edt)

    # When
    utc = tz.toUTC(EAST_02)

    # Then
    print(f"{EAST_02} -> {UTC_02} == {utc} --> ", end="")
    if utc == UTC_02:
        print(OK)
    else:
        print(FAIL)

def test_utc_to_cst():

    print("\ntest_utc_to_cst")

    # Given
    cdt = TimeChangeRule("CDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -300)
    cst = TimeChangeRule("CST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -360)
    tz = Timezone(cst, cdt)

    # When
    loc = tz.toLocal(UTC_02)

    # Then
    print(f"{UTC_02} -> {CENT_02} == {loc} --> ", end="")
    if loc == CENT_02:
        print(OK)
    else:
        print(FAIL)


def test_utc_to_cdt():

    print("\ntest_utc_to_cdt")

    # Given
    cdt = TimeChangeRule("CDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -300)
    cst = TimeChangeRule("CST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -360)
    tz = Timezone(cst, cdt)

    # When
    loc = tz.toLocal(UTC_01)

    # Then
    print(f"{UTC_01} -> {CENT_01} == {loc} --> ", end="")
    if loc == CENT_01:
        print(OK)
    else:
        print(FAIL)

def test_change_rules_est_to_cst():

    print("\ntest_change_rules_est_to_cst")

    # Given
    edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    est = TimeChangeRule("EST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -300)
    cdt = TimeChangeRule("CDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -300)
    cst = TimeChangeRule("CST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -360)
    tz = Timezone(est, edt)

    # When
    eloc = tz.toLocal(UTC_01)

    # Then
    print(f"{UTC_01} -> {EAST_01} == {eloc} --> ", end="")
    if eloc == EAST_01:
        print(OK)
    else:
        print(FAIL)

    # Now When
    tz.setRules(cst, cdt)
    cloc = tz.toLocal(UTC_01)

    # Then
    print(f"{UTC_01} -> {CENT_01} == {cloc} --> ", end="")
    if cloc == CENT_01:
        print(OK)
    else:
        print(FAIL)


def test_utc_is_dst():

    print("\ntest_utc_is_dst")

    # Given
    edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    est = TimeChangeRule("EST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -300)
    tz = Timezone(est, edt)

    # When
    isDst = tz.utcIsDST(UTC_01)

    # Then
    print(f"{UTC_01} == {isDst} --> ", end="")
    if isDst:
        print(OK)
    else:
        print(FAIL)



def test_loc_is_dst():

    print("\ntest_loc_is_dst")

    # Given
    edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    est = TimeChangeRule("EST", utimezone.FIRST,  utimezone.SUN, utimezone.NOV, 2, -300)
    tz = Timezone(est, edt)

    # When
    isDst = tz.locIsDST(EAST_01)

    # Then
    print(f"{EAST_01} == {isDst} --> ", end="")
    if isDst:
        print(OK)
    else:
        print(FAIL)



# Run the tests
test_utc_to_edt()
test_utc_to_est()
test_edt_to_utc()
test_est_to_utc()
test_utc_to_cst()
test_utc_to_cdt()
test_change_rules_est_to_cst()
test_utc_is_dst()
test_loc_is_dst()
print("\n")