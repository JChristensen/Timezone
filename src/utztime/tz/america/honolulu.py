from utztime import utimezone as tz

America_Honolulu = tz.Timezone(
    tz.TimeChangeRule("HST", tz.FIRST, tz.SUN, tz.NOV, 2, -(10 * 60)),
    tz.TimeChangeRule("HDT", tz.SECOND, tz.SUN, tz.MAR, 2, -(9 * 60)),
    'Pacific/Honolulu'
)
