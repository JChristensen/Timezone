import utztime.utimezone as utimezone
from utztime.utimezone import Timezone, TimeChangeRule
import unittest
from .test_rules import UTC_01, UTC_02, EAST_01, EAST_02

EDT = TimeChangeRule("EDT", utimezone.SECOND, utimezone.SUN, utimezone.MAR, 2, -240)
EST = TimeChangeRule("EST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -300)
CST = TimeChangeRule("CST", utimezone.FIRST, utimezone.SUN, utimezone.NOV, 2, -400)


class test_timezone(unittest.TestCase):


    def test_clone_deep(self):

        # Given
        tz = Timezone(name="MyZone", std=EST, dst=EDT)

        # When
        tzClone = tz.clone(name="clone", shallow=False)

        # Then
        assert tzClone._name == "clone"
        assert tz is not tzClone
        assert tz._dst is not tzClone._dst
        assert tz._std is not tzClone._std


    def test_clone_shallow(self):

        # Given
        tz = Timezone(name="MyZone", std=EST, dst=EDT)

        # When
        tzClone = tz.clone(name="clone", shallow=True)

        # Then
        assert tzClone._name == "clone"
        assert tz is not tzClone
        assert tz._dst is tzClone._dst
        assert tz._std is tzClone._std


    def test_link(self):

        # Given
        tz = Timezone(name="MyZone", std=EST, dst=EDT)

        # When
        tzClone = tz.link(name="linked")

        # Then
        assert tzClone._name == "linked"
        assert tz is not tzClone
        assert tz._dst is tzClone._dst
        assert tz._std is tzClone._std



    def test_create_simple_timezone(self):

        # When
        tz = Timezone(name="MyZone", std=EST, dst=EDT)

        # Then
        assert tz is not None


    def test_tz_eq(self):

        # Given
        tz1 = Timezone(name="MyZone", std=EST, dst=EDT)
        tz2 = Timezone(name="MyZone2", std=EST, dst=EDT)

        # Then
        assert tz1 == tz2


    def test_tz_ne(self):

        # Given
        tz1 = Timezone(name="MyZone", std=EST, dst=EDT)
        tz2 = Timezone(name="MyZone2", std=CST, dst=EDT)

        # Then
        assert tz1 != tz2


    def test_tz_gt(self):

        # Given
        tz1 = Timezone(name="MyZone", std=EST, dst=EDT)
        tz2 = Timezone(name="MyZone2", std=CST, dst=EDT)

        # Then
        assert tz1 > tz2


    def test_tz_lt(self):

        # Given
        tz1 = Timezone(name="MyZone", std=CST, dst=EDT)
        tz2 = Timezone(name="MyZone2", std=EST, dst=EDT)

        # Then
        assert tz1 < tz2


    def test_tz_ge(self):

        # Given
        tz1 = Timezone(name="MyZone", std=EST, dst=EDT)
        tz2 = Timezone(name="MyZone2", std=EST, dst=EDT)

        # Then
        assert tz1.__ge__(tz2), "ONE"
        assert tz1 >= tz2, "TWO"


    def test_tz_le(self):

        # Given
        tz1 = Timezone(name="MyZone", std=CST, dst=EDT)
        tz2 = Timezone(name="MyZone2", std=EST, dst=EDT)

        # Then
        assert tz1 <= tz2


    def test_getNamee(self):

        # Given
        name = "MyTZName"
        tz = Timezone(name=name, std=CST, dst=EDT)

        # Then
        assert tz.getName() == name


    def test_to_utc(self):

        # Given
        tz = Timezone(name="MyZone", std=EST, dst=EDT)

        # When
        t = tz.toUTC(EAST_01)

        # Then
        assert t == UTC_01


    def test_to_local(self):

        # Given
        tz = Timezone(name="MyZone", std=EST, dst=EDT)

        # When
        t = tz.toLocal(UTC_01)

        # Then
        assert t == EAST_01


    def test_is_utc_dst(self):

        # Given
        tz = Timezone(name="MyZone", std=EST, dst=EDT)

        # Then
        assert tz.utcIsDST(UTC_01) is True
        assert tz.utcIsDST(UTC_02) is False
        assert tz.utcIsSTD(UTC_01) is False
        assert tz.utcIsSTD(UTC_02) is True


    def test_is_local_dst(self):

        # Given
        tz = Timezone(name="MyZone", std=EST, dst=EDT)

        # Then
        assert tz.utcIsDST(EAST_01) is True
        assert tz.utcIsDST(EAST_02) is False
        assert tz.utcIsSTD(EAST_01) is False
        assert tz.utcIsSTD(EAST_02) is True


    # def test_std_dst_crossover(self):

    #     # Given
    #     tz = Timezone(
    #         name='CST6CDT',
    #         std=TimeChangeRule(abbrev="CST", week=utimezone.FIRST, dow=utimezone.SUN, month=utimezone.NOV, hour=2, offset=-(6 * 60)),
    #         dst=TimeChangeRule(abbrev="CDT", week=utimezone.SECOND, dow=utimezone.SUN, month=utimezone.MAR, hour=2, offset=-(5 * 60)))

    #     # When
    #     stdStart = TZTime.create(2023, 3, 12, 2, 0, 0).time() # 1678608000  # 2023/03/12 02:00:00 1970 Epoch
    #     dstStart = TZTime.create(2023, 11, 5, 2, 0, 0).time() # 1699171200  # 2023/11/05 02:00:00 1970 Epoch
    #     stdEnd = dstStart - 1
    #     dstEnd = stdStart - 1


    #     # When
    #     # stdStart = TZTime.create(year=2023, month=3, day=12, hour=2, min=0, sec=0, tz=tz)
    #     # dstStart = TZTime.create(year=2023, month=11, day=5, hour=2, min=0, sec=0, tz=tz)
    #     # stdEnd = TZTime.create(year=2023, month=11, day=5, hour=1, min=59, sec=0, tz=tz)
    #     # dstEnd = TZTime.create(year=2023, month=3, day=12, hour=1, min=59, sec=0, tz=tz)
    #     # #dstEnd = stdStart.plusSeconds(-1)
    #     #stdEnd = dstStart.plusSeconds(-1)
    #     # stdStartZulu = stdStart.toTimezone(tz=None)
    #     # dstStartZulu = dstStart.toTimezone(tz=None)
    #     # stdEndZulu = stdEnd.toTimezone(tz=None)
    #     # dstEndZulu = dstEnd.toTimezone(tz=None)

    #     # Then
    #     #assert tz.locIsDST(dstStart.time()) == True
    #     #assert tz.locIsDST(stdStart.time()) == False

    #     assert tz.locIsDST(dstStart) == True
    #     assert tz.locIsDST(dstEnd) == True
    #     assert tz.locIsDST(dstStart-100) == False
    #     assert False
    #     # assert tz.locIsSTD(stdStartLoc) == True
    #     # assert tz.utcIsDST(dstStartUtc) == True
    #     # assert tz.utcIsDST(stdStartUtc) == False

    #     # assert tz.locIsDST(stdStartLoc - 1) == True
    #     # assert tz.locIsDST(stdStartUtc - 1) == True



    #     # assert tz.locIsDST(dstEnd.time()) == True
    #     # assert tz.locIsDST(stdEnd.time()) == False

    #     # assert tz.utcIsDST(dstEndZulu.time()) == True
    #     # assert tz.utcIsDST(stdEndZulu.time()) == False





    # # TODO:  More tests around the private internals of the ported class
