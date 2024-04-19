from utztime import utimezone as tz

Canada_Newfoundland = tz.Timezone(
    tz.TimeChangeRule("NST", tz.FIRST, tz.SUN, tz.NOV, 2, -(4 * 60) + 30),
    tz.TimeChangeRule("NDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(3 * 60) + 30),
    'Canada/Newfoundland'
)
