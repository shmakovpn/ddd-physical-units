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
    
    # TODO перенести в Value (Unit + Value) 
    # def test__str(self) -> None:
    #    assert str(tm.m) == f'1{tm.m.label}'
    # 
    # def test__eq(self) -> None:
    #    with pytest.raises(TypeError):
    #        _ = m == UnsupportedType()
    #    
    #    with pytest.raises(TypeError):
    #        _ = m != UnsupportedType()
    #    
    #    assert Meter(value=2) == Meter(value=2)
    #   assert Meter(value=2) != Meter(value=3)
    #
    # def test__mul(self) -> None:
    #    with pytest.raises(TypeError):
    #        m*UnsupportedType()
    #    
    #    with pytest.raises(TypeError):
    #        m*None
    #
    #    assert m*2 == Meter(2)
    #
    # def test__rmul(self) -> None:
    #     with pytest.raises(TypeError):
    #        UnsupportedType()*m
    #    
    #    with pytest.raises(TypeError):
    #        None*m
    #    
    #    assert 3*m == Meter(3)