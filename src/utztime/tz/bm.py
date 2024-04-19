from utztime import utimezone as tz

from .ca import _AST, _ADT

Atlantic_Bermuda = tz.Timezone(std=_AST, dst=_ADT, name='Atlantic/Bermuda')
