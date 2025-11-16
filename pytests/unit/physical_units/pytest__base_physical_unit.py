import dataclasses

import physical_units.base_physical_unit as tm


class TestBasePhysicalUnit:
    def test_inheritance(self) -> None:
        assert len(tm.BasePhysicalUnit.mro()) == 2  # BasePhysicalUnit does not have parents  # noqa: S101
    
    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(tm.BasePhysicalUnit)  # noqa: S101
        