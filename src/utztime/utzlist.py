"""
A utility class where you can define and store your timezones.
You can use each timezone definition yourself, and store them in your own lists.
Or, you can define and assign them here for a more common interface.
Including the built-in sorting by StandardTime
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


def registerTimezone(tz: tz.Timezone):
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


def clear():
    """
    Clear all timezones from the timezone list.
    Mostly helpful for unit-testing.
    """
    _TIMEZONES.clear()
