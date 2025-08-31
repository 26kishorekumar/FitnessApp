import pytest
from app import calculate_bmi

def test_calculate_bmi_correct_value():
    # Test with valid inputs
    result = calculate_bmi(70, 1.75)
    assert result == pytest.approx(22.857), "BMI calculation is incorrect."

def test_calculate_bmi_invalid_input():
    # Test with invalid inputs
    with pytest.raises(ValueError, match="Invalid input for BMI calculation."):
        calculate_bmi("abc", 1.75)  # Invalid weight
        calculate_bmi(70, 0)       # Invalid height (zero)
        calculate_bmi(70, -1.75)   # Invalid height (negative)