import sys

sys.path.insert(0, 'src')

import unittest

if not unittest.main('tests').wasSuccessful():
    sys.exit(1)

sys.path[0] = 'dist'

if not unittest.main('tests').wasSuccessful():
    sys.exit(1)