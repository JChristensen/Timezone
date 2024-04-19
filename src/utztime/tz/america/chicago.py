from utztime import utimezone as tz

America_Chicago = tz.Timezone(
    tz.TimeChangeRule("CST", tz.FIRST, tz.SUN, tz.NOV, 2, -(6 * 60)),
    tz.TimeChangeRule("CDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(5 * 60)),
    'America/Chicago'
)
