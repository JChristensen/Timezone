"""
Simply a list of defined TimeZones you can include in your package, or just copy the one you want.
"""
import utimezone as tz


America_Newfoundland = tz.Timezone(
        tz.TimeChangeRule("NST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(4*60)-30),
        tz.TimeChangeRule("NDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(3*60)-30),
        'America/Newfoundland'
    )

America_Atlantic = tz.Timezone(
        tz.TimeChangeRule("AST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(4*60)),
        tz.TimeChangeRule("ADT", tz.SECOND, tz.SUN, tz.MAR, 2, -(3*60)),
        'America/Atlantic'
    )

America_Eastern = tz.Timezone(
        tz.TimeChangeRule("EST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(5*60)),
        tz.TimeChangeRule("EDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(4*60)),
        'America/Eastern'
    )

America_Central = tz.Timezone(
        tz.TimeChangeRule("CST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(6*60)),
        tz.TimeChangeRule("CDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(5*60)),
        'America/Central'
    )

America_Mountain = tz.Timezone(
        tz.TimeChangeRule("MST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(7*60)),
        tz.TimeChangeRule("MDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(6*60)),
        'America/Mountain'
    )

America_MountainNoDST = tz.Timezone(
        tz.TimeChangeRule("MST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(7*60)),
        tz.TimeChangeRule("MST", tz.SECOND, tz.SUN, tz.MAR, 2, -(7*60)),
        'America/MountainNoDST'
    )

America_Pacific = tz.Timezone(
        tz.TimeChangeRule("PST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(8*60)),
        tz.TimeChangeRule("PDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(7*60)),
        'America/Pacific'
    )

America_Alaska = tz.Timezone(
        tz.TimeChangeRule("AKST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(9*60)),
        tz.TimeChangeRule("AKDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(8*60)),
        'America/Alaska'
    )

America_Hawaii = tz.Timezone(
        tz.TimeChangeRule("HST", tz.FIRST,  tz.SUN, tz.NOV, 2, -(10*60)),
        tz.TimeChangeRule("HDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(9*60)),
        'America/Hawaii'
    )


TIMEZONES = {
    America_Newfoundland._name:     America_Newfoundland,
    America_Atlantic._name:         America_Atlantic,
    America_Eastern._name:          America_Eastern,
    America_Central._name:          America_Central,
    America_Mountain._name:         America_Mountain,
    America_MountainNoDST._name:    America_MountainNoDST,
    America_Pacific._name:          America_Pacific,
    America_Alaska._name:           America_Alaska,
    America_Hawaii._name:           America_Hawaii
    }
