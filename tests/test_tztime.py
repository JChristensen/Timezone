from utztime import TZTime
import utztime.utzlist as tz
import unittest
import time


CDS = (2022, 7, 13, 10, 58, 43)  # Central Daylight Savings Time
CST = (2022, 1, 13, 10, 58, 43)  # Central Standard Time


class TestTZTime(unittest.TestCase):


    def test_create_default_tztime(self):

        # Given
        now = int(time.time())

        # When
        t = TZTime()

        # Then
        assert now <= t.time()


    def test_create_specific_utc_time(self):


        # When
        t = TZTime.create(2001, 2, 3, 4, 5, 6)

        # Then
        assert t.year() == 2001
        assert t.month() == 2
        assert t.day() == 3
        assert t.hour() == 4
        assert t.minute() == 5
        assert t.second() == 6
        assert t.tz() is None


    def test_create_specific_EST_time(self):

        # When
        t = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Eastern)

        # Then
        assert t.year() == 2001
        assert t.month() == 2
        assert t.day() == 3
        assert t.hour() == 4
        assert t.minute() == 5
        assert t.second() == 6
        assert t.tz() == tz.America_Eastern


    def test_UTC_is_before_EST(self):

        # Given
        utc = TZTime.create(2001, 2, 3, 4, 5, 6)
        est = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Eastern)

        # Then
        assert utc < est


    def test_PST_is_after_EST(self):

        # Given
        pst = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Pacific)
        est = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Eastern)

        # Then
        assert pst > est


    def test_time_eq(self):

        # Given
        t1 = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Pacific)
        t2 = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Pacific)
        t3 = TZTime.create(2001, 2, 3, 7, 5, 6, tz.America_Eastern)

        # Then
        assert t1 == t2
        assert t1 == t3
        assert t2 == t3


    def test_time_ne(self):

        # Given
        t1 = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Pacific)
        t2 = TZTime.create(2001, 2, 3, 4, 5, 7, tz.America_Pacific)
        t3 = TZTime.create(2001, 2, 3, 7, 5, 8, tz.America_Eastern)

        # Then
        assert t1 != t2
        assert t1 != t3
        assert t2 != t3


    def test_time_gt(self):

        # Given
        t1 = TZTime.create(2001, 2, 3, 4, 5, 7, tz.America_Pacific)
        t2 = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Pacific)
        t3 = TZTime.create(2001, 2, 3, 7, 5, 6, tz.America_Eastern)

        # Then
        assert t1 > t2
        assert t1 != t2
        assert t1 > t3
        assert t1 != t3


    def test_time_lt(self):

        # Given
        t1 = TZTime.create(2001, 2, 3, 4, 5, 5, tz.America_Pacific)
        t2 = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Pacific)
        t3 = TZTime.create(2001, 2, 3, 7, 5, 6, tz.America_Eastern)

        # Then
        assert t1 < t2
        assert t1 != t2
        assert t1 < t3
        assert t1 != t3


    def test_time_ge(self):

        # Given
        t1 = TZTime.create(2001, 2, 3, 4, 5, 7, tz.America_Pacific)
        t2 = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Pacific)
        t3 = TZTime.create(2001, 2, 3, 7, 5, 6, tz.America_Eastern)

        # Then
        assert t1 >= t2
        assert t1 != t2
        assert t1 >= t3
        assert t1 != t3
        assert t2 >= t3
        assert t3 == t3


    def test_time_le(self):

        # Given
        t1 = TZTime.create(2001, 2, 3, 4, 5, 5, tz.America_Pacific)
        t2 = TZTime.create(2001, 2, 3, 4, 5, 6, tz.America_Pacific)
        t3 = TZTime.create(2001, 2, 3, 7, 5, 6, tz.America_Eastern)

        # Then
        assert t1 <= t2
        assert t1 != t2
        assert t1 <= t3
        assert t1 != t3
        assert t2 <= t3
        assert t3 == t3

