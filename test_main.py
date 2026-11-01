import pytest
from main import parse_chemical_formula, calculate_compound_attenuation

def test_parse_chemical_formula():
    assert parse_chemical_formula("H2O") == {'H': 2, 'O': 1}
    assert parse_chemical_formula("PbO2") == {'Pb': 1, 'O': 2}
    assert parse_chemical_formula("BaSO4") == {'Ba': 1, 'S': 1, 'O': 4}

def test_calculate_compound_attenuation():
    # H2O expected calculation
    # H mass: 2.016, O mass: 15.999, Total = 18.015
    # w_H = 0.1119, w_O = 0.8881
    # mu/rho = (0.1119 * 0.1263) + (0.8881 * 0.0636) ≈ 0.07062
    assert calculate_compound_attenuation("H2O") == 0.07062

def test_invalid_element():
    with pytest.raises(ValueError):
        calculate_compound_attenuation("Xx2O")
