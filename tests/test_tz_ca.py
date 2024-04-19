from utztime.tztime import TZTime
from utztime.utimezone import Timezone
import unittest
import utztime.tz.ca as ca
from . import util


class test_tz_ca(unittest.TestCase):


    def test_std_dst(self):

        # Given - Create UTC times that are known STD and DST for USA
        stdTime = TZTime.create(year=2023, month=11, day=6)
        dstTime = TZTime.create(year=2023, month=3, day=13)

        # When/Then
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=ca.America_St_Johns)
        util.testStdAndDst(stdTime=stdTime, dstTime=dstTime, tz=ca.America_Halifax)
