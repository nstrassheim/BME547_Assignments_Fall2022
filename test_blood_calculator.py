
import pytest 
@pytest.mark.parametrize("value_HDL, expected_HDL",
    [(85, "Normal"),
    (50, "Borderline Low"),
    (35, "low")
    ])
def test_check_HDL(value_HDL, expected_HDL): 
    from blood_calculator import check_HDL
    answer = check_HDL(value_HDL)
    assert answer == expected_HDL

@pytest.mark.parametrize("value_LDL, expected_LDL",
    [(120, "Normal"),
    (145, "Borderline High"),
    (170, "High"),
    (200, "Very High")
    ])
def test_check_LDL(value_LDL, expected_LDL): 
    from blood_calculator import check_LDL
    answer = check_LDL(value_LDL)
    assert answer == expected_LDL

@pytest.mark.parametrize("value_total, expected_total",
    [(150, "Normal"),
    (220, "Borderline High"),
    (300, "High"),
    ])
def test_check_total(value_total, expected_total): 
    from blood_calculator import check_total
    answer = check_total(value_total)
    assert answer == expected_total
