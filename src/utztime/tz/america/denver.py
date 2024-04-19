from utztime import utimezone as tz

America_Denver = tz.Timezone(
    tz.TimeChangeRule("MST", tz.FIRST, tz.SUN, tz.NOV, 2, -(7 * 60)),
    tz.TimeChangeRule("MDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(6 * 60)),
    'America/Denver'
)
