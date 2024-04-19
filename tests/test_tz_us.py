from utztime.tztime import TZTime
from utztime.utimezone import Timezone
import unittest
import utztime.tz.us as us
from . import util


class test_tz_us(unittest.TestCase):


    def test_std_dst(self):

        # Given - Create UTC times that are known STD and DST for USA
        stdTime = TZTime.create(year=2023, month=11, day=6)
        dstTime = TZTime.create(year=2023, month=3, day=13)

        # When/Then
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=us.America_Honolulu, expectStd=True, expectDst=False)  # Phoenix does not do DST
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=us.America_Anchorage)
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=us.America_Los_Angeles)
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=us.America_Denver)
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=us.America_Phoenix, expectStd=True, expectDst=False)  # Phoenix does not do DST
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=us.America_Chicago)
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=us.America_New_York)
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=us.CST, expectStd=True, expectDst=False)
