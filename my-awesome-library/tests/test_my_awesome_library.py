import pytest
from my_awesome_library import example_function, Calculator

def test_example_function():
    assert example_function() == "Hello from my-awesome-library"

def test_calculator():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(7, 4) == 3
