import sys

sys.path.insert(0, 'dist')

import unittest

if not unittest.main('tests').wasSuccessful():
    sys.exit(1)