from .. import utimezone as tz

# Rules
_HST = tz.TimeChangeRule(abbrev="HST", whichDow=tz.FIRST, dow=tz.SUN, month=tz.NOV, hour=2, offset=-(10 * 60))
_AKST = tz.TimeChangeRule(abbrev="AKST", whichDow=tz.FIRST, dow=tz.SUN, month=tz.NOV, hour=2, offset=-(9 * 60))
_AKDT = tz.TimeChangeRule(abbrev="AKDT", whichDow=tz.SECOND, dow=tz.SUN, month=tz.MAR, hour=2, offset=-(8 * 60))
_PST = tz.TimeChangeRule(abbrev="PST", whichDow=tz.FIRST, dow=tz.SUN, month=tz.NOV, hour=2, offset=-(8 * 60))
_PDT = tz.TimeChangeRule(abbrev="PDT", whichDow=tz.SECOND, dow=tz.SUN, month=tz.MAR, hour=2, offset=-(7 * 60))
_MST = tz.TimeChangeRule(abbrev="MST", whichDow=tz.FIRST, dow=tz.SUN, month=tz.NOV, hour=2, offset=-(7 * 60))
_MDT = tz.TimeChangeRule(abbrev="MDT", whichDow=tz.SECOND, dow=tz.SUN, month=tz.MAR, hour=2, offset=-(6 * 60))
_CST = tz.TimeChangeRule(abbrev="CST", whichDow=tz.FIRST, dow=tz.SUN, month=tz.NOV, hour=2, offset=-(6 * 60))
_CDT = tz.TimeChangeRule(abbrev="CDT", whichDow=tz.SECOND, dow=tz.SUN, month=tz.MAR, hour=2, offset=-(5 * 60))
_EST = tz.TimeChangeRule(abbrev="EST", whichDow=tz.FIRST, dow=tz.SUN, month=tz.NOV, hour=2, offset=-(5 * 60))
_EDT = tz.TimeChangeRule(abbrev="EDT", whichDow=tz.SECOND, dow=tz.SUN, month=tz.MAR, hour=2, offset=-(4 * 60))


# Canonical Zones
America_Honolulu = tz.Timezone(name='Pacific/Honolulu', std=_HST, dst=None)
America_Anchorage = tz.Timezone(name='America/Anchorage', std=_AKST, dst=_AKDT)
America_Los_Angeles = tz.Timezone(name='America/Los_Angeles', std=_PST, dst=_PDT)
America_Phoenix = tz.Timezone(name='America/Phoenix', std=_MST, dst=None)
America_Denver = tz.Timezone(name='America/Denver', std=_MST, dst=_MDT)
America_Chicago = tz.Timezone(name='America/Chicago', std=_CST, dst=_CDT)
America_New_York = tz.Timezone(name='America/New_York', std=_EST, dst=_EDT, )
CST = tz.Timezone(name="CST", std=_CST, dst=None)

# Linked Zones
EST5EDT = America_New_York.link(name="EST5EDT")
CST6CDT = America_Chicago.link(name="CST6CDT")
MST7MDT = America_Denver.link("MST7MDT")
MST = America_Phoenix.link(name="MST")
PST8PDT = America_Los_Angeles.link(name="PST8PDT")
HST = America_Honolulu.link(name="HST")
