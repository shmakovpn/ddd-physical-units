from .formula import Formula

"""
7 основных (base) физических величин (quantities) СИ
 - Длина — метр (m)
 - Масса — килограмм (kg)
 - Время — секунда (s)
 - Сила электрического тока — ампер (A)
 - Термодинамическая температура — кельвин (K)
 - Количество вещества — моль (mol)
 - Сила света — кандела (cd)

Остальные физические величины (quantities) производные (derived)
"""


class Unit:
    """
    Единица измерения (unit) физической величины (quantity)
    """
    formula: Formula

    _instances_by_formula: dict[Formula, Unit] = {}
    """{formula: unit}"""

    def __init__(self, formula: Formula) -> None:
        self.formula: Formula = formula
    
    def __str__(self) -> str:
        if self.label is not None:
            return self.label
        return str(self.formula)
    
    def __new__(cls, formula: Formula) -> Unit:
        """Не бывает двух единиц измерения (unit) с одинаковыми формулами"""
        instance: Unit | None = cls._instances_by_formula.get(formula)
        
        if instance is None:
            # единица измерения с такой формулой не существует
            new_instance: Unit = super().__new__(cls)
            cls._instances_by_formula[formula] = new_instance
        
        return instance
