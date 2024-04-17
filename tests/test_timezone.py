import utztime.utimezone as utimezone
from utztime.utimezone import Timezone, TimeChangeRule
import unittest
from .test_rules import UTC_01, UTC_02, EAST_01, EAST_02


class TestTimezone(unittest.TestCase):

    EDT = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
    EST = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
    CST = TimeChangeRule("CST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -400)


    def test_create_simple_timezone(self):

        # When
        tz = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")

        # Then
        assert tz is not None


    def test_tz_eq(self):

        # Given
        tz1 = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")
        tz2 = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")

        # Then
        assert tz1 == tz2


    def test_tz_ne(self):

        # Given
        tz1 = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")
        tz2 = Timezone(TestTimezone.CST, TestTimezone.EDT, "MyZone")

        # Then
        assert tz1 != tz2


    def test_tz_gt(self):

        # Given
        tz1 = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")
        tz2 = Timezone(TestTimezone.CST, TestTimezone.EDT, "MyZone")

        # Then
        assert tz1 > tz2


    def test_tz_lt(self):

        # Given
        tz1 = Timezone(TestTimezone.CST, TestTimezone.EDT, "MyZone")
        tz2 = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")

        # Then
        assert tz1 < tz2


    def test_tz_ge(self):

        # Given
        tz1 = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")
        tz2 = Timezone(TestTimezone.CST, TestTimezone.EDT, "MyZone")

        # Then
        assert tz1.__ge__(tz2), "ONE"
        assert tz1 >= tz2, "TWO"


    def test_tz_le(self):

        # Given
        tz1 = Timezone(TestTimezone.CST, TestTimezone.EDT, "MyZone")
        tz2 = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")

        # Then
        assert tz1 <= tz2


    def test_getNamee(self):

        # Given
        name = "MyTZName"
        tz = Timezone(TestTimezone.CST, TestTimezone.EDT, name)

        # Then
        assert tz.getName() == name


    def test_to_utc(self):

        # Given
        tz = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")

        # When
        t = tz.toUTC(EAST_01)

        # Then
        assert t == UTC_01


    def test_to_local(self):

        # Given
        tz = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")

        # When
        t = tz.toLocal(UTC_01)

        # Then
        assert t == EAST_01


    def test_is_utc_dst(self):

        # Given
        tz = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")

        # When
        isDst = tz.utcIsDST(UTC_01)
        isNotDst = tz.utcIsDST(UTC_02)

        # Then
        assert isDst is True
        assert isNotDst is False


    def test_is_local_dst(self):

        # Given
        tz = Timezone(TestTimezone.EST, TestTimezone.EDT, "MyZone")

        # When
        isDst = tz.utcIsDST(EAST_01)
        isNotDst = tz.utcIsDST(EAST_02)

        # Then
        assert isDst is True
        assert isNotDst is False


    # TODO:  More tests around the private internals of the ported class
