from utztime import utimezone as tz

Atlantic_Bermuda = tz.Timezone(
    tz.TimeChangeRule("AST", tz.FIRST, tz.SUN, tz.NOV, 2, -(4 * 60)),
    tz.TimeChangeRule("ADT", tz.SECOND, tz.SUN, tz.MAR, 2, -(3 * 60)),
    'Atlantic/Bermuda'
)
