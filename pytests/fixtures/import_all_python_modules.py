import importlib
import pathlib
import sys
import types

import pytest

__all__ = (
    'import_all_python_src_modules__fixture',
)


@pytest.fixture(scope='session')
def import_all_python_src_modules__fixture() -> list[types.ModuleType]:
    """Import all python modules in the project's ./src directory."""
    root = pathlib.Path(__file__).resolve().parent.parent.parent
    src_path = root / "src"

    if not src_path.exists():
        raise RuntimeError(f"No src directory found at: {src_path}")

    # Ensure src/ is in PYTHONPATH
    sys.path.insert(0, str(src_path))

    # Find all .py files except __init__.py
    py_files = src_path.rglob("*.py")

    imported_modules = []

    for file in py_files:
        if file.name == "__init__.py":
            continue

        # Make a module name like: package.subpackage.module
        module_rel = file.relative_to(src_path).with_suffix("")
        module_name = ".".join(module_rel.parts)

        module = importlib.import_module(module_name)
        imported_modules.append(module)

    return imported_modules
