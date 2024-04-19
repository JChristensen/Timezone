from utztime import utimezone as tz

America_New_York = tz.Timezone(
    tz.TimeChangeRule("EST", tz.FIRST, tz.SUN, tz.NOV, 2, -(5 * 60)),
    tz.TimeChangeRule("EDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(4 * 60)),
    'America/New_York'
)
