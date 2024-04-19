"""
Root package.

**To simply access the TZTime class**
```python
from utztime import TZTime
```

**Access to the timezone and rules classes**
```python
from utztime import TimeChangeRule, Timezone
```

**Access to the pre-defined list of timezones**
```python
import utztime.tz.us
import utztime.tz.ca
```

**To Populate the tzlist registry**
```python
import utztime.tz.us
import utztime.tzlist
utztime.tzlist.registerTimezone(utztime.tz.us.America_Los_Angeles)
utztime.tzlist.registerTimezone(utztime.tz.us.America_Chicago)
utztime.tzlist.registerTimezone(utztime.tz.us.America_Phoenix)
utztime.tzlist.registerTimezone(utztime.tz.us.America_New_York)
```

There is a `EPOCH` const that can be used here if desired.  It is the uPython EPOCH of Jan 1 2000. Not the unix EPOCH of Jan 1 1970.
This EPOCH value is self adjusting to the platforms actual EPOCH
```python
from utztime import EPOCH
```

"""

import time
from .tztime import TZTime  # noqa: F401, F403
from .utimezone import Timezone, TimeChangeRule  # noqa: F401, F403

EPOCH = TZTime.create(time.gmtime(0)[0], 1, 1, 0, 0, 0)
