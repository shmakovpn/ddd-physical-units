import dataclasses
from typing import TYPE_CHECKING

from .exceptions import EmptyFormulaError

if TYPE_CHECKING:
    from .type_hints import Denominator, Numerator

__all__ = (
    'Formula',
)


@dataclasses.dataclass(frozen=True)
class Formula:
    """
    Формула единицы измерения.
    У каждой единицы измерения, будь то производная или основная, есть своя уникальная формула.
    Не бывает разных единиц измерения с одинаковыми формулами.
    """
    numerator: Numerator
    """
    Числитель (numerator) производной (derived) или основной (base) физической величины.
    """
    denominator: Denominator
    """
    Единицы измерения в знаменателе производной (derived) физической величины (quantity).
    Например: Паскаль будет иметь знаменатель `m**2`
    """

    def __post_init__(self) -> None:
        if len(self.numerator) == 0 and len(self.denominator) == 0:
            raise EmptyFormulaError('Формула не может быть пустой')

    def is_base_unit(self) -> bool:
        """
        True если формула соответствует основной (base) единице измерения.
        False если формула соответствует производной (derived) единице измерения.
        """
        if len(self.numerator) == 1 and len(self.denominator) == 0:
            return True
        else:
            return False
