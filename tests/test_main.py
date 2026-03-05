import pytest
from main import add_numbers, multiply_numbers


class TestAddNumbers:
    """Tests for add_numbers function - this will be COVERED"""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        assert add_numbers(2, 3) == 5
        assert add_numbers(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add_numbers(-5, -3) == -8
        assert add_numbers(-10, 5) == -5

    def test_add_zero(self):
        """Test adding zero"""
        assert add_numbers(0, 5) == 5
        assert add_numbers(5, 0) == 5


class TestMultiplyNumbers:
    """Tests for multiply_numbers function - this will be COVERED"""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers"""
        assert multiply_numbers(2, 3) == 6
        assert multiply_numbers(5, 4) == 20

    def test_multiply_with_zero(self):
        """Test multiplying with zero"""
        assert multiply_numbers(0, 5) == 0
        assert multiply_numbers(5, 0) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply_numbers(-2, 3) == -6
        assert multiply_numbers(-2, -3) == 6

    def test_special_function(self):
        """Test the special_function"""
        from main import special_function
        assert special_function(0, 0) == 8
# Note: divide_numbers and print_hi are NOT tested
# This will show up as uncovered code in the coverage report
