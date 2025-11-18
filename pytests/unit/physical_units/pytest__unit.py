import physical_units.unit as tm
from physical_units.formula import Formula


class UnsupportedType:
    """some stub type for experiments with unsupported types"""
    pass


class TestUnit:
    def test_inheritance(self) -> None:
        assert len(tm.Unit.mro()) == 2  # Unit does not have parents

    # У основной единицы измерения label должен совпадать 


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