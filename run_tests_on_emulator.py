
import mip
mip.install("unittest")
import unittest

import sys

sys.path.insert(0, 'src')

if not unittest.main('tests').wasSuccessful():
    sys.exit(1)

sys.path[0] = 'dist'

if not unittest.main('tests').wasSuccessful():
    sys.exit(1)