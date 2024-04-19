import utztime.utzlist as tzl
from utztime import utimezone
from utztime.utimezone import TimeChangeRule, Timezone
import unittest
from utztime.tz.america.new_york import America_New_York
from utztime.tz.america.chicago import America_Chicago
from utztime.tz.america.phoenix import America_Phoenix
from utztime.tz.america.los_angeles import America_Los_Angeles


class TestTZList(unittest.TestCase):


    def setUp(self):

        tzl.clear()
        tzl.setTimezone(America_New_York)
        tzl.setTimezone(America_Chicago)
        tzl.setTimezone(America_Los_Angeles)
        tzl.setTimezone(America_Phoenix)



    def test_find_timezone(self):

        # Given
        name = "America/Chicago"

        # When
        tz = tzl.getTimezone(name)

        # Then
        assert tz is not None
        assert tz.getName() == name


    def test_find_timezone_case_insensitive(self):

        # Given
        name = "AmerIcA/ChiCAGo"

        # When
        tz = tzl.getTimezone(name)

        # Then
        assert tz is not None
        assert tz.getName() != name
        assert tz.getName().upper() == name.upper()


    def test_find_invalid_timezone(self):

        # Given
        name = "NotA/Timezone"

        # When
        tz = tzl.getTimezone(name)

        # Then
        assert tz is None


    def test_add_new_timezone(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        name = "Australia/Sydney"
        tz = Timezone(est, edt, name)
        preListSize = len(tzl.getTimezones())

        # When
        tzl.setTimezone(tz)

        # Then
        assert len(tzl.getTimezones()) == (preListSize + 1)
        assert tzl.getTimezone(name) is not None
        assert tzl.getTimezone(name) == tz


    def test_overwrite_timezone(self):

        # Given
        edt = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
        est = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
        name = "America/Phoenix"
        tz = Timezone(est, edt, name)
        preListSize = len(tzl.getTimezones())

        # When
        tzl.setTimezone(tz)
        newTZ = tzl.getTimezone(name)

        # Then
        assert newTZ is not None
        assert tz == newTZ
        assert newTZ._std == est
        assert len(tzl.getTimezones()) == (preListSize)
        assert tzl.getTimezone(name) is not None
        assert tzl.getTimezone(name) == tz


    def test_list_sorted_by_standard_offset(self):


        # Given
        lst = tzl.getTimezones()

        # Then
        prevTz = None
        prevOffset = 999999999
        for tz in lst:
            assert tz._std.offset <= prevOffset, f"{tz._std.offset} <= {prevOffset} on {tz} {prevTz}"
            prevTz = tz
            prevOffset = tz._std.offset


    def test_list_maintains_sorted_by_standard_offset(self):


        # Given
        edt = TimeChangeRule("AEDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, (60 * 11))
        est = TimeChangeRule("AEST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, (60 * 10))
        name = "Australia/Sydney"
        tz = Timezone(est, edt, name)

        # When
        tzl.setTimezone(tz)
        lst = tzl.getTimezones()

        # Then
        assert lst[0] == tz


    def test_get_list_names_is_only_strings(self):

        # Given
        nameList = tzl.getTimezoneNames()

        # Then
        for name in nameList:
            assert isinstance(name, str)


    def test_get_list_names_matches_main_list(self):

        # Given
        tzList = tzl.getTimezones()
        nameList = tzl.getTimezoneNames()

        # Then
        assert len(tzList) == len(nameList)
        for index, name in enumerate(nameList):
            assert name == tzList[index].getName()
