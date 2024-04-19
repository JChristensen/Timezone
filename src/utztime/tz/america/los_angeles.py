from utztime import utimezone as tz

America_Los_Angeles = tz.Timezone(
    tz.TimeChangeRule("PST", tz.FIRST, tz.SUN, tz.NOV, 2, -(8 * 60)),
    tz.TimeChangeRule("PDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(7 * 60)),
    'America/Los_Angeles'
)
