from utztime.tztime import TZTime
from utztime.utimezone import Timezone
import unittest
import utztime.tz.bm as bm
from . import util


class test_tz_bm(unittest.TestCase):


    def test_std_dst(self):

        # Given - Create UTC times that are known STD and DST for USA
        stdTime = TZTime.create(year=2023, month=11, day=6)
        dstTime = TZTime.create(year=2023, month=3, day=13)

        # When/Then
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=bm.Atlantic_Bermuda)
