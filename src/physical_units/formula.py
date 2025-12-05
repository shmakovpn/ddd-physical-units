import dataclasses
from typing import TYPE_CHECKING

from .exceptions import EmptyFormulaError

if TYPE_CHECKING:
    from .type_hints import Denominator, Numerator, UnitLabel

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

    def is_base_unit(self) -> bool:
        """
        True если формула соответствует основной (base) единице измерения.
        False если формула соответствует производной (derived) единице измерения.
        """
        if len(self.numerator) == 1 and len(self.denominator) == 0:
            return True
        else:
            return False
    
    @staticmethod
    def _reduce_fraction(numerator: Numerator, denominator: Denominator):
        numerator_accumulator = list(numerator)
        denominator_accumulator = list(denominator)

        for unit_label_1 in numerator:
            for unit_label_2 in denominator_accumulator:
                if unit_label_1 == unit_label_2:
                    numerator_accumulator.remove(unit_label_1)
                    denominator_accumulator.remove(unit_label_2)
                    break
        
        return tuple(numerator_accumulator), tuple(denominator_accumulator)
    
    def __mul__(self, value: Formula) -> Formula:
        if not isinstance(value, Formula):
            raise TypeError(f'unsupported type "{type(value).__name__}" for __mul__')
        # перемножение формул должно поддерживать сокращение дробей
        left_numerator: list[UnitLabel] = list(self.numerator)
        right_numerator: list[UnitLabel] = list(value.numerator)
        left_denominator: list[UnitLabel] = list(self.denominator)
        right_denominator: list[UnitLabel] = list(value.denominator)

        unit: UnitLabel
        # for unit in left_numerator:
