import dataclasses

from .exceptions import (
    EmptyInDenominatorError,
    EmptyInNumeratorError,
    NoneBaseUnitLabelError,
    NoneInDenominatorError,
    NoneInNumeratorError,
    UnitFormulaAlreadyRegisteredError,
    UnitLabelAlreadyRegisteredError,
    UnregisteredLabelInFormulaError,
    WrongBaseNumeratorError,
)
from .formula import Formula
from .type_hints import Denominator, Numerator, UnitLabel

__all__ = (
    'Unit',
    'Quantity',
    'm', 'meter',
    's', 'second',
    'kg', 'kilogram',
    'N', 'newton',
)

"""
7 основных физических величин (quantities) СИ
 - Длина — метр (m)
 - Масса — килограмм (kg)
 - Время — секунда (s)
 - Сила электрического тока — ампер (A)
 - Термодинамическая температура — кельвин (K)
 - Количество вещества — моль (mol)
 - Сила света — кандела (cd)
"""


class Unit:
    """Base for physical units"""
    label: UnitLabel | None
    """
    The abbreviated name of a physical quantity, for example, "m" for meters, "s" for seconds.
    """
    formula: Formula
    """Формула единицы измерения"""
    
    class Registry:
        """Реестр единиц измерения. Статический класс"""
        _instances_by_label: dict[UnitLabel, Unit] = {}
        """{label: unit}"""
        _instances_by_formula: dict[Formula, Unit] = {}
        """{(numerator, denominator): unit}"""

        @classmethod
        def get_physical_unit(cls, formula: Formula) -> Unit | None:
            instance: Unit | None = cls._instances_by_formula.get(formula)
            return instance
        
        @classmethod
        def register_physical_unit(cls, physical_unit: Unit, formula: Formula, label: UnitLabel | None) -> None:
            if label is None:
                # регистрируем в реестре единицу измерения без label
                cls._instances_by_formula[formula] = physical_unit
                return None
            if label in cls._instances_by_label:
                # такой label уже зарегистрирован
                msg = f'label="{label}" уже зарегистрирован в "{cls._instances_by_label[label]}"'
                raise UnitLabelAlreadyRegisteredError(msg)
            # В формулу не должно попадать незарегистрированных label
            formula_label_set: set[UnitLabel] = set(formula.numerator) | set(formula.denominator)
            label_set: set[UnitLabel] = set(cls._instances_by_label.keys()) | {label}
            diff_label_set: set[UnitLabel] = formula_label_set - label_set
            if diff_label_set:
                raise UnregisteredLabelInFormulaError(f'Незарегистрированные label в формуле: {diff_label_set}')
                
            # регистрируем единицу измерения в реестре
            cls._instances_by_label[label] = physical_unit
            cls._instances_by_formula[formula] = physical_unit
            return None
    
    @classmethod
    def _validate_label_and_formula(cls, label: str | None, formula: Formula) -> None:
        if formula.is_base_unit():
            if label is None:
                msg = 'У базовой единицы измерения label не может быть None'
                raise NoneBaseUnitLabelError(msg)
            
            if label != formula.numerator[0]:
                msg = 'У базовой единицы измерения label должен совпадать с numerator[0]'
                raise WrongBaseNumeratorError(msg)
        
        if None in formula.numerator:
            msg = 'Не должно быть None в числителе'
            raise NoneInNumeratorError(msg)
        
        if None in formula.denominator:
            msg = 'Не должно быть None в знаменателе'
            raise NoneInDenominatorError(msg)
        
        if '' in formula.numerator:
            msg = 'Не должно быть пустых строк в числителе'
            raise EmptyInNumeratorError(msg)
        
        if '' in formula.denominator:
            msg = 'Не должно быть пустых строк в знаменателе'
            raise EmptyInDenominatorError(msg)

    def __new__(cls, label: str | None, formula: Formula) -> Unit:
        cls._validate_label_and_formula(label=label, formula=formula)
        instance: Unit | None = cls.Registry.get_physical_unit(formula=formula)
        if instance:
            # единица измерения с такой формулой уже существует
            if instance.label != label:
                # пытаемся создать уже имеющуюся единицу измерения под другим именем
                msg = (
                    f'Единица измерения "{instance}" уже зарегистрирована, '
                    f'нельзя применить новый label="{label}"'
                )
                raise UnitFormulaAlreadyRegisteredError(msg)
            return instance
        else:
            # единица измерения с такой формулой не существует
            new_instance: Unit = super().__new__(cls)
            # регистрируем единицу измерения в реестре
            cls.Registry.register_physical_unit(physical_unit=new_instance, formula=formula, label=label)
            return new_instance
    
    def __init__(self, label: str | None, formula: Formula) -> None:
        self.label = label
        self.formula = formula
    
    def __str__(self) -> str:
        if self.label is not None:
            return self.label
        return str(self.formula)

    def __eq__(self, value: Unit) -> bool:
        if id(self) == id(value):
            return True
        
        if isinstance(value, type(self)):
            # метр можно сравнить только с метром.
            # сравнение метра с килограммом является ошибкой
            raise ValueError(f'cannot compare "{value}" with "{self}"')
        
        raise TypeError(f'cannot compare type "{type(value).__name__}" with "{self}"')

    def __mul__(self, value: int | float | complex | Unit) -> Unit:
        if isinstance(value, (int, float, complex)):
            result: Quantity = Quantity(value=value, unit=self)
            return result
        
        if isinstance(value, type(self)):
            # TODO продолжить
            right_numerator = list(value.formula.numerator)
        
        raise TypeError(f'unsupported type "{type(value).__name__}" for __mul__ in "{self.__class__.__name__}"')
    
    def __rmul__(self, value: int | float | complex | Unit) -> Unit:
        result = self * value
        return result


@dataclasses.dataclass(frozen=True)
class Quantity:
    """
    Значение физическая величины (quantity)
    """
    value: float
    """Значение"""
    unit: Unit
    """Единица изменения"""
    

m = meter = Unit(
    label='m', 
    formula=Formula(
        numerator=Numerator('m', ), 
        denominator=Denominator(),
    )
)
"""
Метр. Единица измерения расстояния.
"""

s = second = Unit(
    label='s',
    formula=Formula(
        numerator=Numerator('s', ),
        denominator=Denominator(),
    )
)
"""
Секунда. Единица измерения времени.
"""


kg = kilogram = Unit(
    label='kg',
    formula=Formula(
        numerator=Numerator(('kg', )),
        denominator=Denominator(),
    )
)
"""Килограмм. Единица измерения массы"""


empty = Unit(
    # Пустая строка выбрана специально, чтобы физическая величина (quantity) без единицы измерения
    # не искажала вывод таких величин (quantities) в виде строк.
    # Например: пять метров - 5m, а просто пять - 5.
    label='',  
    formula=Formula(
        numerator=Numerator(),
        denominator=Denominator(),
    )
)
"""
Физическая величина (quantity) без единицы измерения,
например, количество в штуках.
"""

meter_per_second = Unit(
    label=None,
    formula=Formula(
        numerator=Numerator('m', ),
        denominator=Denominator('s', ),
    ),
)
"""м/с - единица измерения скорости"""

N = newton = Unit(
    label='N',
    formula=Formula(
        numerator=Numerator(('kg', 'm')),
        denominator=Denominator(('s', 's')),
    )
)
"""Ньютон, единица измерения силы"""
