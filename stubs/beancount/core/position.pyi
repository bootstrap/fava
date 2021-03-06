# pylint: disable=all
# flake8: noqa
from typing import Any
from typing import NamedTuple
from typing import Optional

from beancount.core.amount import Amount as Amount
from beancount.core.amount import CURRENCY_RE as CURRENCY_RE
from beancount.core.display_context import (
    DEFAULT_FORMATTER as DEFAULT_FORMATTER,
)
from beancount.core.number import D as D
from beancount.core.number import Decimal as Decimal
from beancount.core.number import NUMBER_RE as NUMBER_RE
from beancount.core.number import ZERO as ZERO

Cost: Any
CostSpec: Any

def cost_to_str(cost: Any, dformat: Any, detail: bool = ...): ...

CURRENCY_ORDER: Any
NCURRENCIES: Any

def get_position(posting: Any): ...
def to_string(pos: Any, dformat: Any = ..., detail: bool = ...): ...

class _Position(NamedTuple):
    units: Amount
    cost: Cost

class Position(_Position):
    cost_types: Any = ...
    def __new__(cls, units: Any, cost: Optional[Any] = ...): ...
    def __hash__(self) -> Any: ...
    def to_string(self, dformat: Any = ..., detail: bool = ...): ...
    def __eq__(self, other: Any) -> Any: ...
    def sortkey(self): ...
    def __lt__(self, other: Any) -> Any: ...
    def __copy__(self): ...
    def currency_pair(self): ...
    def get_negative(self): ...
    __neg__: Any = ...
    def __abs__(self): ...
    def __mul__(self, scalar: Any): ...
    def is_negative_at_cost(self): ...
    @staticmethod
    def from_string(string: Any): ...
    @staticmethod
    def from_amounts(units: Any, cost_amount: Optional[Any] = ...): ...

from_string: Any
from_amounts: Any
