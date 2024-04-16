import sys
import unittest

if not unittest.main('tests').wasSuccessful():
    sys.exit(1)