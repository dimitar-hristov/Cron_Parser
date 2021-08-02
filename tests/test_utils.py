import pytest
from utils.utils import is_syntax_valid, process_expression, values_are_in_range

@pytest.mark.parametrize(
"expression, expected_output", 
    [
        ("*", True),
        ("*/15", True),
        ("1-10", True),
        ("12-20", True),
        ("10,2,3,25", True),
        ("22", True),
        ("**", False),
        ("*15", False),
        ("-12--20", False),
        ("1-", False),
        ("1,", False),
        ("", False),
    ]
)
def test_is_syntax_valid(expression, expected_output):
    actual = is_syntax_valid(expression=expression)
    assert expected_output == actual


@pytest.mark.parametrize(
"expression, min_value, max_value, expected_output", 
    [
        ("*", 0, 10, True),
        ("*/15", 0, 20, True),
        ("1-20", 0, 20, True),
        ("12-20", 0, 20, True),
        ("10,2,3,25", 0, 30, True),
        ("22", 0, 30, True),
        ("*/15", 0, 14, False),
        ("1-21", 0, 20, False),
        ("1,2,35,25", 0, 30, False),
        ("220", 0, 30, False),      
    ]
)
def test_values_are_in_range(expression, min_value, max_value, expected_output):
    actual = values_are_in_range(expression=expression, min_value=min_value, max_value=max_value)
    assert expected_output == actual


@pytest.mark.parametrize(
"expression, min_value, max_value, expected_output", 
    [
        ("*", 0, 10, "0 1 2 3 4 5 6 7 8 9 10"),
        ("*/15", 0, 20, "0 15"),
        ("1-5", 0, 20, "1 2 3 4 5"),
        ("1,2,3,25", 0, 30, "1 2 3 25"),
        ("22", 0, 30, "22"),
    ]
)
def test_process_expression(expression, min_value, max_value, expected_output):
    actual = process_expression(expression=expression, min_value=min_value, max_value=max_value)
    assert expected_output == actual