import pytest
from main import count_well_formed_parenthesis

def test_known_values():
    assert count_well_formed_parenthesis(1) == 1
    assert count_well_formed_parenthesis(2) == 2
    assert count_well_formed_parenthesis(3) == 5
    assert count_well_formed_parenthesis(4) == 14
    assert count_well_formed_parenthesis(5) == 42

def test_bounds():
    with pytest.raises(ValueError):
        count_well_formed_parenthesis(0)
    with pytest.raises(ValueError):
        count_well_formed_parenthesis(16)

def test_performance():
    for n in range(1, 16):
        assert count_well_formed_parenthesis(n) > 0