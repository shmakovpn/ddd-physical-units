from physical_units.type_hints import Denominator, Numerator


class TestNumerator:
    def test_numerator(self) -> None:
        """Проверяем, что числитель (Numerator) это кортеж"""
        assert isinstance(Numerator(), tuple)
        assert Numerator((1, 2)) == (1, 2)


class TestDenominator:
    def test_denominator(self) -> None:
        """Проверяем, что знаменатель  (Denominator) это кортеж"""
        assert isinstance(Denominator(), tuple)
        assert Denominator((1, 2)) == (1, 2)
