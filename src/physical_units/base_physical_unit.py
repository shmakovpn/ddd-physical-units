from dataclasses import dataclass

__all__ = (
    'BasePhysicalUnit',
)


@dataclass
class BasePhysicalUnit:
    """Base for physical units"""
    value: int | float | complex
    """the value of a physical quantity"""
    label: str
    """The abbreviated name of a physical quantity, for example, "m" for meters, "s" for seconds."""


