from utztime import utimezone as tz

America_Anchorage = tz.Timezone(
    tz.TimeChangeRule("AKST", tz.FIRST, tz.SUN, tz.NOV, 2, -(9 * 60)),
    tz.TimeChangeRule("AKDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(8 * 60)),
    'America/Anchorage'
)
