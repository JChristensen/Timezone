"""
Root package.

**To simply access the TZTime class**
```python
from utztime import TZTime
```

**Access to the time zone rules**
```python
from utztime.utimezone import TimeChangeRule, Timezone
```

**Access to the pre-defined list of timezones**
```python
import utztime.tzlist
```

There is a `EPOCH` const that can be used here if desired.  It is the uPython EPOCH of Jan 1 2000. Not the unix EPOCH of Jan 1 1970
```python
EPOCH
```

"""

from .tztime import TZTime  # noqa: F401, F403


"""
Simple Access to the EPOCH value. Unlike non-micropython devices which use an EPOCH of Jan 1 1970.
The Micropython EPOCH is (Jan 1 2000 0:0:0 UTC)
"""
EPOCH = TZTime.create(2000, 1, 1, 0, 0, 0, None)

