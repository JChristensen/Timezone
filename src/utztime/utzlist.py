"""
Simply a list of defined TimeZones you can include in your package, or just copy the one you want.

See the source file directly for a list of pre-defined TimeZones.

The timezones are stored in sort order of the offset value of the StandardTime of each zone.

```python
America_Newfoundland
America_Atlantic
America_Eastern
America_Central
America_Mountain
America_MountainNoDST
America_Pacific
America_Alaska
America_Hawaii
```

"""
from . import utimezone as tz

_TIMEZONES: list[tz.Timezone] = []


def getTimezones() -> list[tz.Timezone]:
    """
    Return a COPY list of registered timezones. Sorted by Standard Time Offset (reverse) Highest to Lowest.
    """
    return _TIMEZONES.copy()


def getTimezoneNames() -> list[str]:
    """
    Return a COPY list of the registered timezone names.  Sorted by Standard Time Offset (reverse) Highest to Lowest
    """
    return [z.getName() for z in _TIMEZONES]


def getTimezone(tzname: str) -> tz.Timezone | None:
    """
    Find the timezone for the provided tz standard string.
    This only references the pre-defined list of available timezones
    within this module. This lookup is case insensitive.
    Timezones are immutable.
    """
    tzname = tzname.upper()
    try:
        return next(z for z in _TIMEZONES if z.getName().upper() == tzname)
    except StopIteration:
        return None


def setTimezone(tz: tz.Timezone):
    """
    Set/Add to the internal list of available timezones.
    This simply makes the provided timezone accessible
    through the getTimezone() function
    """
    assert tz is not None, "Cannot add a None timezone"
    assert tz._name is not None, "Cannot add a timezone without a name"

    try:
        index = next(i for i, z in enumerate(_TIMEZONES) if z.getName() == tz.getName())
        _TIMEZONES[index] = tz
    except StopIteration:
        _TIMEZONES.append(tz)

    _TIMEZONES.sort(reverse=True)


# These pre defined timezones, are in order here of first-to-last on the globe.

America_Newfoundland = tz.Timezone(
    tz.TimeChangeRule("NST", tz.FIRST, tz.SUN, tz.NOV, 2, -(4 * 60) + 30),
    tz.TimeChangeRule("NDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(3 * 60) + 30),
    'Canada/Newfoundland'
)

America_Atlantic = tz.Timezone(
    tz.TimeChangeRule("AST", tz.FIRST, tz.SUN, tz.NOV, 2, -(4 * 60)),
    tz.TimeChangeRule("ADT", tz.SECOND, tz.SUN, tz.MAR, 2, -(3 * 60)),
    'Atlantic/Bermuda'
)

America_Eastern = tz.Timezone(
    tz.TimeChangeRule("EST", tz.FIRST, tz.SUN, tz.NOV, 2, -(5 * 60)),
    tz.TimeChangeRule("EDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(4 * 60)),
    'America/New_York'
)

America_Central = tz.Timezone(
    tz.TimeChangeRule("CST", tz.FIRST, tz.SUN, tz.NOV, 2, -(6 * 60)),
    tz.TimeChangeRule("CDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(5 * 60)),
    'America/Chicago'
)

America_Mountain = tz.Timezone(
    tz.TimeChangeRule("MST", tz.FIRST, tz.SUN, tz.NOV, 2, -(7 * 60)),
    tz.TimeChangeRule("MDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(6 * 60)),
    'America/Denver'
)

America_MountainNoDST = tz.Timezone(
    tz.TimeChangeRule("MST", tz.FIRST, tz.SUN, tz.NOV, 2, -(7 * 60)),
    tz.TimeChangeRule("MST", tz.SECOND, tz.SUN, tz.MAR, 2, -(7 * 60)),
    'America/Phoenix'
)

America_Pacific = tz.Timezone(
    tz.TimeChangeRule("PST", tz.FIRST, tz.SUN, tz.NOV, 2, -(8 * 60)),
    tz.TimeChangeRule("PDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(7 * 60)),
    'America/Los_Angeles'
)

America_Alaska = tz.Timezone(
    tz.TimeChangeRule("AKST", tz.FIRST, tz.SUN, tz.NOV, 2, -(9 * 60)),
    tz.TimeChangeRule("AKDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(8 * 60)),
    'America/Anchorage'
)

America_Hawaii = tz.Timezone(
    tz.TimeChangeRule("HST", tz.FIRST, tz.SUN, tz.NOV, 2, -(10 * 60)),
    tz.TimeChangeRule("HDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(9 * 60)),
    'Pacific/Honolulu'
)


def _setDefaultTimezones():
    """
    Pre-SEt, and re-Set the build-in timezone list.
    Helpful for unit-testing
    """
    _TIMEZONES.clear()
    setTimezone(America_Newfoundland)
    setTimezone(America_Atlantic)
    setTimezone(America_Eastern)
    setTimezone(America_Central)
    setTimezone(America_Mountain)
    setTimezone(America_MountainNoDST)
    setTimezone(America_Pacific)
    setTimezone(America_Hawaii)


_setDefaultTimezones()
