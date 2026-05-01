import pytest
from calculator import calculate_simple_interest, calculate_compound_interest, calculate_tax


def test_simple_interest_basic():
    assert calculate_simple_interest(1000, 5, 2) == 100.0
    assert calculate_simple_interest(500, 10, 1) == 50.0

def test_simple_interest_zero():
    assert calculate_simple_interest(0, 5, 2) == 0.0
    assert calculate_simple_interest(1000, 0, 2) == 0.0

def test_simple_interest_negative():
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
        calculate_simple_interest(-100, 5, 2)
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
        calculate_simple_interest(100, -5, 2)


def test_compound_interest_basic():
    # 1000 * (1 + 10/(100*1))**(1*2) = 1210.0
    assert calculate_compound_interest(1000, 10, 2, 1) == pytest.approx(1210.0)
    assert calculate_compound_interest(1000, 10, 2, 4) == pytest.approx(1218.40, abs=1e-2)

def test_compound_interest_zero():
    assert calculate_compound_interest(0, 5, 2, 1) == 0.0
    assert calculate_compound_interest(1000, 0, 2, 1) == 1000.0

def test_compound_interest_invalid():
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, -1, 1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, 0)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, 2.5)


def test_tax_basic():
    assert calculate_tax(1000, 20) == 200.0
    assert calculate_tax(500, 12.5) == 62.5

def test_tax_zero():
    assert calculate_tax(1000, 0) == 0.0
    assert calculate_tax(0, 15) == 0.0

def test_tax_invalid_rate():
    with pytest.raises(ValueError):
        calculate_tax(1000, -5)
    with pytest.raises(ValueError):
        calculate_tax(1000, 105)
