import pytest


@pytest.mark.parametrize("HDL_value, expected_value", [
    (60, "Normal"),
    (45, "Borderline Low"),
    (15, "Low"),
    (75, "Normal")])
def test_hdl_analysis(HDL_value, expected_value):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(HDL_value)
    expected = expected_value
    assert answer == expected
