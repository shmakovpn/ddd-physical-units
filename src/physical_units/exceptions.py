__all__ = (
    'UnitLabelAlreadyRegisteredError',
    'UnitFormulaAlreadyRegisteredError',
    'EmptyFormulaError',
    'NoneBaseUnitLabelError',
    'WrongBaseNumeratorError',
    'NoneInNumeratorError',
    'NoneInDenominatorError',
    'EmptyInNumeratorError',
    'EmptyInDenominatorError',
)


class UnitLabelAlreadyRegisteredError(RuntimeError):
    """Единица измерения с таким label уже зарегистрирована"""


class UnitFormulaAlreadyRegisteredError(RuntimeError):
    """
    Единица измерения с такой формулой уже зарегистрирована.
    Попытка создать единицу измерения с имеющейся формулой, но другим label
    """


class EmptyFormulaError(ValueError):
    """
    Попытка создать единицу измерения с пустой формулой
    """


class NoneBaseUnitLabelError(ValueError):
    """У базовой единицы измерения label не может быть None"""


class WrongBaseNumeratorError(ValueError):
    """У базовой единицы измерения label должен совпадать с numerator[0]"""


class NoneInNumeratorError(ValueError):
    """Не должно быть None в числителе"""


class NoneInDenominatorError(ValueError):
    """Не должно быть None в знаменателе"""


class EmptyInNumeratorError(ValueError):
    """Не должно быть пустых строк в числителе"""


class EmptyInDenominatorError(ValueError):
    """Не должно быть пустых строк в знаменателе"""
