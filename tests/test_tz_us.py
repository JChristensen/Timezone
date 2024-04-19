from utztime.tztime import TZTime
from utztime.utimezone import Timezone
import unittest
import utztime.tz.us as us


class TestTZUS(unittest.TestCase):
    pass


    # def test_America_Los_Angeles(self):

    #     # Given
    #     tz = us.America_Los_Angeles
    #     stdStart = TZTime.create(year=2024, month=3, day=10, hour=2, min=0, sec=0)
    #     dstStart = TZTime.create(year=2024, month=3, day=10, hour=2, min=0, sec=0)
    #     stdEnd = TZTime.create(year=2024, month=3, day=10, hour=2, min=0, sec=0)

    #     # When
    #     tzClone = tz.clone(name="clone", shallow=False)

    #     # Then
    #     assert tzClone._name == "clone"
    #     assert tz is not tzClone
    #     assert tz._dst is not tzClone._dst
    #     assert tz._std is not tzClone._std


