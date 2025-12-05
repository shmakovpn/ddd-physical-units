import pytest

import physical_units.unit as tm
from physical_units.formula import Formula


class UnsupportedType:
    """some stub type for experiments with unsupported types"""
    pass


class TestUnit:
    def test_inheritance(self) -> None:
        assert len(tm.Unit.mro()) == 2  # Unit does not have parents
    
    def test__validate_label_and_formula(self) -> None:
        # Не должно быть None в числителе
        with pytest.raises(tm.NoneInNumeratorError):
            _ = tm.Unit(
                label='hello', formula=Formula(numerator=tm.Numerator(('m', None)), denominator=tm.Denominator())
            )
        
        # Не должно быть None в знаменателе
        with pytest.raises(tm.NoneInDenominatorError):
            _ = tm.Unit(label='a', formula=Formula(numerator=tm.Numerator(), denominator=tm.Denominator((None, ))))
        
        # Не должно быть пустых строк в числителе
        with pytest.raises(tm.EmptyInNumeratorError):
            _ = tm.Unit(label='hello', formula=Formula(numerator=tm.Numerator(('m', '')), denominator=tm.Denominator()))
        
        # Не должно быть пустых строк в знаменателе
        with pytest.raises(tm.EmptyInDenominatorError):
            _ = tm.Unit(label='a', formula=Formula(numerator=tm.Numerator(), denominator=tm.Denominator(('m', ''))))
        
        # У основной единицы измерения label не может быть None
        with pytest.raises(tm.NoneBaseUnitLabelError):
            _ = tm.Unit(label=None, formula=Formula(numerator=tm.Numerator('m'), denominator=tm.Denominator()))
        
        # У основной единицы измерения label должен совпадать с numerator[0], numerator
        with pytest.raises(tm.WrongBaseNumeratorError):
            _ = tm.Unit(label='s', formula=Formula(numerator=tm.Numerator('m'), denominator=tm.Denominator()))
        
        # TODO в формулу не должно попадать незарегистрированных label. 
        # TODO Именно незарегистрированных, а не базовых. Например: `Н*м` для момента силы


class TestMeter:
    def test_type(self) -> None:
        assert isinstance(tm.meter, tm.Unit)

    def test_singleton(self) -> None:
        pass

    def test__srt(self) -> None:
        assert str(tm.meter) == tm.meter.label
    
    def test__eq(self) -> None:
        assert tm.m == tm.meter

        with pytest.raises(ValueError):
            _ = tm.m == tm.s
        
        with pytest.raises(TypeError):
            _ = tm.m == UnsupportedType()
    
    def test__mul(self) -> None:
        # проверяем умножение на число
        result = tm.m * 3
        assert isinstance(result, tm.Quantity)
        assert result.value == 3
        assert result.unit == tm.m

        # проверяем умножение на неподдерживаемый тип
        with pytest.raises(TypeError):
            _ = tm.m * UnsupportedType()
        
        # проверяем умножение на другую единицу измерения
        square_meter = tm.m * tm.m

    
    def test__rmul(self) -> None:
        # проверяем умножение на число
        result = 3 * tm.m
        assert isinstance(result, tm.Quantity)
        assert result.value == 3
        assert result.unit == tm.m

        # проверяем умножение на неподдерживаемый тип
        with pytest.raises(TypeError):
            _ = UnsupportedType() * tm.m
