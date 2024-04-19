from utztime import utimezone, TZTime
from utztime.utimezone import TimeChangeRule, Timezone
import unittest
import sys
from . import util


# timestamps within Daylight Savings Time (Jan 01 1970 Epochs)
UTC_01 = util.unixToUpyTime(1657745923)   # (2022, 7, 13, 15, 58, 43)
EAST_01 = util.unixToUpyTime(1657731523)  # (2022, 7, 13, 11, 58, 43)
CENT_01 = util.unixToUpyTime(1657727923)  # (2022, 7, 13, 10, 58, 43)

# timestamps within Standard Time
UTC_02 = util.unixToUpyTime(1642111123)   # (2022, 1, 13, 15, 58, 43)
EAST_02 = util.unixToUpyTime(1642093123)  # (2022, 1, 13, 10, 58, 43)
CENT_02 = util.unixToUpyTime(1642089523)  # (2022, 1, 13, 9, 58, 43)


class TestRules(unittest.TestCase):


    def test_rule_to_time_eastern(self):

        # Given
        EST = TimeChangeRule(abbrev="EST", whichDow=utimezone.FIRST, dow=utimezone.SUN, month=utimezone.NOV, hour=2, offset=-(5 * 60))
        EDT = TimeChangeRule(abbrev="EDT", whichDow=utimezone.SECOND, dow=utimezone.SUN, month=utimezone.MAR, hour=2, offset=-(4 * 60))

        # When
        tST = EST.toTime(2023)
        tDS = EDT.toTime(2023)

        # Then
        assert tST == util.unixToUpyTime(1699171200), f"{tST} == {util.unixToUpyTime(1699171200)}"
        assert tDS == util.unixToUpyTime(1678608000), f"{tDS} == {util.unixToUpyTime(1678608000)}"
        assert tST == TZTime.create(2023, 11, 5, 2, 0, 0).time()
        assert tDS == TZTime.create(2023, 3, 12, 2, 0, 0).time()


    def test_rule_to_time_with_which_dow(self):

        # Given
        FIRST = TimeChangeRule(abbrev="EST", whichDow=utimezone.FIRST, dow=utimezone.SUN, month=utimezone.NOV, hour=2, offset=-(5 * 60))
        SECOND = TimeChangeRule(abbrev="EST", whichDow=utimezone.SECOND, dow=utimezone.SUN, month=utimezone.NOV, hour=2, offset=-(5 * 60))
        THIRD = TimeChangeRule(abbrev="EST", whichDow=utimezone.THIRD, dow=utimezone.SUN, month=utimezone.NOV, hour=2, offset=-(5 * 60))
        FORTH = TimeChangeRule(abbrev="EST", whichDow=utimezone.FOURTH, dow=utimezone.SUN, month=utimezone.NOV, hour=2, offset=-(5 * 60))
        LAST = TimeChangeRule(abbrev="EST", whichDow=utimezone.LAST, dow=utimezone.SUN, month=utimezone.NOV, hour=2, offset=-(5 * 60))

        # When
        first = FIRST.toTime(2023)
        second = SECOND.toTime(2023)
        third = THIRD.toTime(2023)
        forth = FORTH.toTime(2023)
        last = LAST.toTime(2023)

        # Then (these 2 values are CORRECT.  Figure out why the calc is wrong )
        assert first == TZTime.create(2023, 11, 5, 2, 0, 0).time()
        assert second == TZTime.create(2023, 11, 12, 2, 0, 0).time()
        assert third == TZTime.create(2023, 11, 19, 2, 0, 0).time()
        assert forth == TZTime.create(2023, 11, 26, 2, 0, 0).time()
        assert last == TZTime.create(2023, 11, 26, 2, 0, 0).time()



    def test_clone(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)

        # When
        edtClone = edt.clone()

        # Then
        assert edt is not edtClone


    def test_equals(self):

        # Given
        edt1 = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        edt2 = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        edt3 = TimeChangeRule("EDT3", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        edt4 = TimeChangeRule("EDT4", utimezone.FIRST, utimezone.SUN, utimezone.MAR, 2, -240)
        edt5 = TimeChangeRule("EDT5", utimezone.SECOND, utimezone.MON, utimezone.MAR, 2, -240)
        edt6 = TimeChangeRule("EDT6", utimezone.SECOND, utimezone.SUN, utimezone.FEB, 2, -240)
        edt7 = TimeChangeRule("EDT7", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 3, -240)
        edt8 = TimeChangeRule("EDT8", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -241)

        # Then
        assert edt1 == edt2
        assert edt1 == edt3
        assert edt1 != edt4
        assert edt1 != edt5
        assert edt1 != edt6
        assert edt1 != edt7
        assert edt1 != edt8


    def test_utc_to_edt(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(name="Zone", std=est, dst=edt)

        # When
        loc = tz.toLocal(UTC_01)

        # Then
        assert loc == EAST_01, f"{loc} == {EAST_01}"


    def test_utc_to_est(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(name="Zone", std=est, dst=edt)

        # When
        loc = tz.toLocal(UTC_02)

        # Then
        assert loc == EAST_02, f"{loc} == {EAST_02}"


    def test_edt_to_utc(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(name="Zone", std=est, dst=edt)

        # When
        utc = tz.toUTC(EAST_01)

        # Then
        assert utc == UTC_01, f"{utc} == {UTC_01}"


    def test_est_to_utc(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(name="Zone", std=est, dst=edt)

        # When
        utc = tz.toUTC(EAST_02)

        # Then
        assert utc == UTC_02, f"{utc} == {UTC_02}"


    def test_utc_to_cst(self):

        # Given
        cdt = TimeChangeRule("CDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -300)
        cst = TimeChangeRule("CST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -360)
        tz = Timezone(name="Zone", std=cst, dst=cdt)

        # When
        loc = tz.toLocal(UTC_02)

        # Then
        assert loc == CENT_02, f"{loc} == {CENT_02}"


    def test_utc_to_cdt(self):

        # Given
        cdt = TimeChangeRule("CDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -300)
        cst = TimeChangeRule("CST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -360)
        tz = Timezone(name="Zone", std=cst, dst=cdt)

        # When
        loc = tz.toLocal(UTC_01)

        # Then
        assert loc == CENT_01, f"{loc} == {CENT_01}"


    def test_utc_is_dst(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(name="Zone", std=est, dst=edt)

        # When
        isDst = tz.utcIsDST(UTC_01)

        # Then
        assert isDst, f"isDst == {isDst}"


    def test_loc_is_dst(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        tz = Timezone(name="Zone", std=est, dst=edt)

        # When
        isDst = tz.locIsDST(EAST_01)

        # Then
        assert isDst, f"isDst == {isDst}"
