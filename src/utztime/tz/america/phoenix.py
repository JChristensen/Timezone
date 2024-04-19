from utztime import utimezone as tz

America_Phoenix = tz.Timezone(
    tz.TimeChangeRule("MST", tz.FIRST, tz.SUN, tz.NOV, 2, -(7 * 60)),
    tz.TimeChangeRule("MST", tz.SECOND, tz.SUN, tz.MAR, 2, -(7 * 60)),
    'America/Phoenix'
)
