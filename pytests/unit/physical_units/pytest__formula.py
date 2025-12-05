import pytest

import physical_units.formula as tm
from physical_units.type_hints import Denominator, Numerator


class TestFormula:
    def test_inheritance(self) -> None:
        assert len(tm.Formula.mro()) == 2  # Formula не имеет предков

    def test_empty_formula(self) -> None:
        """Проверяем, что можно создать пустую формулу"""
        _ = tm.Formula(Numerator(), Denominator())

    @pytest.mark.parametrize(
        ('numerator', 'denominator', 'is_base'), 
        [
            (Numerator('a'), Denominator(), True),
            (Numerator(('a', 'a')), Denominator(), False),
            (Numerator(), Denominator('b'), False),
            (Numerator('a'), Denominator('b'), False),
        ]
    )
    def test_is_base_unit(self, numerator, denominator, is_base) -> None:  # noqa: ANN001
        assert tm.Formula(numerator=numerator, denominator=denominator).is_base_unit() is is_base
    
    @pytest.mark.parametrize(
        ('numerator', 'denominator', 'result_numerator', 'result_denominator'),
        [
            (('a', 'b'), ('c', 'd'), ('a', 'b'), ('c', 'd')),
            (('a', 'b'), ('a', 'c'), ('b',), ('c',)),
            (('a', 'a', 'b'), ('a', 'c'), ('a', 'b'), ('c',)),
            ( ('a', ), ('a', 'b'), tuple(), ('b', ) ),
            (('a', ), ('a'), tuple(), tuple())
        ]
    )
    def test__reduce_fraction(self, numerator, denominator, result_numerator, result_denominator) -> None: # noqa: ANN001
        assert tm.Formula._reduce_fraction(numerator, denominator) == (result_numerator, result_denominator)
