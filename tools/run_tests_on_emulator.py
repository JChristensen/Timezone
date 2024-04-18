
import mip
mip.install("unittest")
import unittest

import os
import sys

# Extract and set a new base-path from this tools directory
basePath = '/'.join(sys.path[0].split('/')[:-1])
sys.path[0] = basePath

#sys.path.insert(0, basePath)
sys.path.insert(0, f"src")

print(f"sys.path = {sys.path}")
if not unittest.main('tests').wasSuccessful():
    sys.exit(1)

sys.path[0] = f"dist"

print(f"sys.path = {sys.path}")
if not unittest.main('tests').wasSuccessful():
    sys.exit(1)