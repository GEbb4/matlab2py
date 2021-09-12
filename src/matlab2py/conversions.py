"""
Unit conversions.
"""
from matlab2py.handles import GraphicsRootHandle

_dpi = GraphicsRootHandle().ScreenPixelsPerInch

POINTS_PER_INCH = 72
CENTIMETERS_PER_INCH = 2.54

def raise_not_implemented(*args, **kwargs):
    """Raises NotImplementedError (for use in lambdas)."""
    raise NotImplementedError()

# It's easier to do stuff in inches because matplotlib works in inches.
# These dicts define the conversion functions.
_TO_INCHES = {
    "pixels": lambda x: x / _dpi,
    "inches": lambda x: x,
    "centimeters": lambda x: x / CENTIMETERS_PER_INCH,
    "points": lambda x: x / POINTS_PER_INCH,
    "characters": raise_not_implemented,
    "normalized": raise_not_implemented,
}
_FROM_INCHES = {
    "pixels": lambda x: x * _dpi,
    "inches": lambda x: x,
    "centimeters": lambda x: x * CENTIMETERS_PER_INCH,
    "points": lambda x: x * POINTS_PER_INCH,
    "characters": raise_not_implemented,
    "normalized": raise_not_implemented,
}

def to_inches(val, unit):
    """Convert val in unit to inches."""
    return _TO_INCHES[unit](val)

def from_inches(unit, val):
    """Convert val in inches to unit."""
    return _FROM_INCHES[unit](val)
