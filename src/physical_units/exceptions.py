__all__ = (
    'UnitLabelAlreadyRegisteredError',
    'UnitFormulaAlreadyRegisteredError',
    'EmptyFormulaError',
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