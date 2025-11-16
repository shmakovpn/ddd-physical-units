import types


class TestAll:
    """Checks that all python modules (exclude __init__.py) has '__all__'"""
    def test__all(self, import_all_python_src_modules__fixture: list[types.ModuleType]) -> None:
        module: types.ModuleType

        for module in import_all_python_src_modules__fixture:
            assert isinstance(module.__all__, (list, tuple))  # noqa: S101
