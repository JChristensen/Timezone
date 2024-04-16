from utztime import utimezone
from utztime.utimezone import TimeChangeRule, Timezone
import unittest
import sys


# timestamps within Daylight Savings Time (Jan 01 1970 Epochs)
UTC_01 = 1657745923   # (2022, 7, 13, 15, 58, 43)
EAST_01 = 1657731523  # (2022, 7, 13, 11, 58, 43)
CENT_01 = 1657727923  # (2022, 7, 13, 10, 58, 43)

# timestamps within Standard Time
UTC_02 = 1642111123   # (2022, 1, 13, 15, 58, 43)
EAST_02 = 1642093123  # (2022, 1, 13, 10, 58, 43)
CENT_02 = 1642089523  # (2022, 1, 13, 9, 58, 43)

# upython and unix python, use 2 different EPOCHs
UPYTHON_EPOCH = 946706400  # (2000, 1, 1, 0, 0, 0)

if sys.implementation.name == "micropython":
    UTC_01 -= UPYTHON_EPOCH
    EAST_01 -= UPYTHON_EPOCH
    CENT_01 -= UPYTHON_EPOCH
    UTC_02 -= UPYTHON_EPOCH
    EAST_02 -= UPYTHON_EPOCH
    CENT_02 -= UPYTHON_EPOCH


class TestZones(unittest.TestCase):


    def test_utc_to_edt(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(est, edt)

        # When
        loc = tz.toLocal(UTC_01)

        # Then
        assert loc == EAST_01, f"{loc} == {EAST_01}"


    def test_utc_to_est(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(est, edt)

        # When
        loc = tz.toLocal(UTC_02)

        # Then
        assert loc == EAST_02, f"{loc} == {EAST_02}"


    def test_edt_to_utc(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(est, edt)

        # When
        utc = tz.toUTC(EAST_01)

        # Then
        assert utc == UTC_01, f"{utc} == {UTC_01}"


    def test_est_to_utc(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(est, edt)

        # When
        utc = tz.toUTC(EAST_02)

        # Then
        assert utc == UTC_02, f"{utc} == {UTC_02}"


    def test_utc_to_cst(self):

        # Given
        cdt = TimeChangeRule("CDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -300)
        cst = TimeChangeRule("CST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -360)
        tz = Timezone(cst, cdt)

        # When
        loc = tz.toLocal(UTC_02)

        # Then
        assert loc == CENT_02, f"{loc} == {CENT_02}"


    def test_utc_to_cdt(self):

        # Given
        cdt = TimeChangeRule("CDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -300)
        cst = TimeChangeRule("CST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -360)
        tz = Timezone(cst, cdt)

        # When
        loc = tz.toLocal(UTC_01)

        # Then
        assert loc == CENT_01, f"{loc} == {CENT_01}"


    def test_change_rules_est_to_cst(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        cdt = TimeChangeRule("CDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -300)
        cst = TimeChangeRule("CST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -360)
        tz = Timezone(est, edt)

        # When
        eloc = tz.toLocal(UTC_01)

        # Then
        assert eloc == EAST_01

        # Now When
        tz.setRules(cst, cdt)
        cloc = tz.toLocal(UTC_01)

        # Then
        assert cloc == CENT_01, f"{cloc} == {CENT_01}"


    def test_utc_is_dst(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(est, edt)

        # When
        isDst = tz.utcIsDST(UTC_01)

        # Then
        assert isDst, f"isDst == {isDst}"


    def test_loc_is_dst(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(est, edt)

        # When
        isDst = tz.locIsDST(EAST_01)

        # Then
        assert isDst, f"isDst == {isDst}"
