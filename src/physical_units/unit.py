
from .exceptions import UnitFormulaAlreadyRegisteredError, UnitLabelAlreadyRegisteredError
from .formula import Formula
from .type_hints import Denominator, Numerator, UnitLabel

__all__ = (
    'BasePhysicalUnitOld',
)

"""
7 основных физических величин СИ
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
            else:
                # регистрируем единицу измерения в реестре
                cls._instances_by_label[label] = physical_unit
                cls._instances_by_formula[formula] = physical_unit
                return None

    def __new__(cls, label: str | None, formula: Formula) -> Unit:
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
        return f'{self.value!r}{self.label}'

    def __eq__(self, value: Unit) -> bool:
        if not isinstance(value, self.__class__):
            raise TypeError(f'unable to compare "{type(value).__name__}" with "{self.__class__.__name__}"')

        if self.value == value.value:
            return True
        
        return False

    def __mul__(self, value: int | float | complex | Unit) -> Unit:
        if isinstance(value, (int, float, complex)):
            result: Unit = self.__class__(value=self.value * value)
            return result
        
        raise TypeError(f'unsupported type "{type(value).__name__}" for __mul__ in "{self.__class__.__name__}"')
    
    def __rmul__(self, value: int | float | complex | Unit) -> Unit:
        result = self * value
        return result
    

m = meter = Unit(
    label='m', 
    formula=Formula(
        numerator=Numerator('m', ), 
        denominator=Denominator(),
    )
)
