from .. import utimezone as tz
from . import us

# Rules
_NST = tz.TimeChangeRule(abbrev="NST", whichDow=tz.FIRST, dow=tz.SUN, month=tz.NOV, hour=2, offset=-(4 * 60) + 30)
_NDT = tz.TimeChangeRule(abbrev="NDT", whichDow=tz.SECOND, dow=tz.SUN, month=tz.MAR, hour=2, offset=-(3 * 60) + 30)
_AST = tz.TimeChangeRule(abbrev="AST", whichDow=tz.FIRST, dow=tz.SUN, month=tz.NOV, hour=2, offset=-(4 * 60))
_ADT = tz.TimeChangeRule(abbrev="ADT", whichDow=tz.SECOND, dow=tz.SUN, month=tz.MAR, hour=2, offset=-(3 * 60))

# Canonical Zones
America_St_Johns = tz.Timezone(name='America/St_Johns', std=_NST, dst=_NDT)
America_Halifax = tz.Timezone(name='America/Halifax', std=_AST, dst=_ADT)

# Linked Zones
America_Vancouver = us.PST8PDT.link(name="America/Vancouver")
America_Edmonton = us.MST7MDT.link(name="America/Edmonton")
America_Whitehorse = us.MST.link(name="America/Whitehorse")
America_Winnipeg = us.CST6CDT.link(name="America/Winnipeg")
America_Regina = us.CST.link(name="America/Regina")
America_Toronto = us.EST5EDT.link(name="America/Toronto")

Canada_Atlantic = America_Halifax.link(name="Canada/Atlantic")
Canada_Central = America_Winnipeg.link(name="Canada/Central")
Canada_Eastern = America_Toronto.link(name="Canada/Eastern")
Canada_Mountain = America_Edmonton.link(name="Canada/Mountain")
Canada_Newfoundland = America_St_Johns.link(name="Canada/Newfoundland")
Canada_Pacific = America_Vancouver.link(name="Canada/Pacific")
Canada_Saskatchewan = America_Regina.link(name="Canada/Saskatchewan")
Canada_Yukon = America_Whitehorse.link(name="Canada/Yukon")
