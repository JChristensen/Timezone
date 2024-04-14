"""
Simply a list of defined TimeZones you can include in your package, or just copy the one you want.
"""
from . import utimezone as tz
from ucollections import OrderedDict


America_Newfoundland = tz.Timezone(
        tz.TimeChangeRule("NST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(4*60)-30),
        tz.TimeChangeRule("NDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(3*60)-30),
        'Canada/Newfoundland'
    )

America_Atlantic = tz.Timezone(
        tz.TimeChangeRule("AST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(4*60)),
        tz.TimeChangeRule("ADT", tz.SECOND, tz.SUN, tz.MAR, 2, -(3*60)),
        'Atlantic/Bermuda'
    )

America_Eastern = tz.Timezone(
        tz.TimeChangeRule("EST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(5*60)),
        tz.TimeChangeRule("EDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(4*60)),
        'America/New_York'
    )

America_Central = tz.Timezone(
        tz.TimeChangeRule("CST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(6*60)),
        tz.TimeChangeRule("CDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(5*60)),
        'America/Chicago'
    )

America_Mountain = tz.Timezone(
        tz.TimeChangeRule("MST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(7*60)),
        tz.TimeChangeRule("MDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(6*60)),
        'America/Denver'
    )

America_MountainNoDST = tz.Timezone(
        tz.TimeChangeRule("MST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(7*60)),
        tz.TimeChangeRule("MST", tz.SECOND, tz.SUN, tz.MAR, 2, -(7*60)),
        'America/Phoenix'
    )

America_Pacific = tz.Timezone(
        tz.TimeChangeRule("PST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(8*60)),
        tz.TimeChangeRule("PDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(7*60)),
        'America/Los_Angeles'
    )

America_Alaska = tz.Timezone(
        tz.TimeChangeRule("AKST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(9*60)),
        tz.TimeChangeRule("AKDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(8*60)),
        'America/Anchorage'
    )

America_Hawaii = tz.Timezone(
        tz.TimeChangeRule("HST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(10*60)),
        tz.TimeChangeRule("HDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(9*60)),
        'Pacific/Honolulu'
    )



TIMEZONES = OrderedDict()
TIMEZONES[America_Newfoundland._name] =     America_Newfoundland
TIMEZONES[America_Atlantic._name] =         America_Atlantic
TIMEZONES[America_Eastern._name] =          America_Eastern
TIMEZONES[America_Central._name] =          America_Central
TIMEZONES[America_Mountain._name] =         America_Mountain
TIMEZONES[America_MountainNoDST._name] =    America_MountainNoDST
TIMEZONES[America_Pacific._name] =          America_Pacific
TIMEZONES[America_Alaska._name] =           America_Alaska
TIMEZONES[America_Hawaii._name] =           America_Hawaii


def getTimezone(tzname: str) -> tz.Timezone:
    """
    Find the timezone for the provided tz standard string
    """
    if tzname not in TIMEZONES.keys():
        return None
    return TIMEZONES[tzname]

