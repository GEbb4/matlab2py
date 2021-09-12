"""
Tests for the conversions module.
"""
from unittest import TestCase

import pytest
from parameterized import parameterized

from matlab2py.conversions import from_inches, to_inches

class TestConversions(TestCase):

    @parameterized.expand(
        [
            ("inches", 1, 1, None),
            ("centimeters", 2.54, 1, None),
            ("pixels", 96, 1, None),
            ("points", 72, 1, None),
            ("characters", 1, 1, NotImplementedError),
            ("normalized", 1, 1, NotImplementedError),
        ]
    )
    def test_to_inches(self, unit, val, exp_inches, raises):
        """Test that to_inches behaves as expected."""

        if raises is not None:
            with pytest.raises(raises):
                inches = to_inches(val, unit)
        else:
            inches = to_inches(val, unit)
            self.assertEqual(inches, exp_inches)

    @parameterized.expand(
        [
            ("inches", 1, 1, None),
            ("centimeters", 1, 2.54, None),
            ("pixels", 1, 96, None),
            ("points", 1, 72, None),
            ("characters", 1, 1, NotImplementedError),
            ("normalized", 1, 1, NotImplementedError),
        ]
    )
    def test_from_inches(self, unit, inches, exp_val, raises):
        """Test that from_inches behaves as expected."""

        if raises is not None:
            with pytest.raises(raises):
                val = from_inches(unit, inches)
        else:
            val = from_inches(unit, inches)
            self.assertEqual(val, exp_val)
