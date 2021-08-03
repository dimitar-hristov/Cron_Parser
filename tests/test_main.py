import sys
from unittest.mock import patch

import pytest

from src.main import main
from utils import const


@pytest.mark.parametrize(
    "input",
    [
        (["script", "foo"]),
        (["script"]),
        (["script", "foo bar baz x y"]),
        (["script", "foo bar baz x y z a"]),
        (["script", "foo,bar,baz,x,y,z"]),
    ],
)
def test_main_missing_args(input):
    mock_args = input
    with patch.object(sys, "argv", mock_args):
        actual = main()
        expcted = (
            "Cron Expression Parser. \n"
            "You need to provide a single string specifying: \n"
            "\t- minutes; \n"
            "\t- hours \n"
            "\t- day of month \n"
            "\t- month \n"
            "\t- day of week; \n"
            "\t- and the command as a cron expression."
        )
        assert actual == expcted


def test_main_invalid_syntax(mocker):
    mocker.patch.object(sys, "argv", ["script", "foo bar baz x y command"])
    mock_arg = mocker.Mock()
    mock_arg.value = "mock_args"
    mocker.patch.object(const, "ORDER_OF_ARGS", [mock_arg])
    mock_min_max = mocker.patch("main.const.ARGS_MIN_AND_MAX_VALUES")
    mock_min_max.get.return_value = ["mock_min_value", "mock_max_value"]
    mocker.patch("main.utils.is_syntax_valid", return_value=False)

    with pytest.raises(ValueError) as e:
        main()
    expcted_error = "Argument for `mock_args` has invalid value!"

    assert str(e.value) == expcted_error


def test_main_value_not_in_range(mocker):
    mocker.patch.object(sys, "argv", ["script", "foo bar baz x y command"])
    mock_arg = mocker.Mock()
    mock_arg.value = "mock_args"
    mocker.patch.object(const, "ORDER_OF_ARGS", [mock_arg])
    mock_min_max = mocker.patch("main.const.ARGS_MIN_AND_MAX_VALUES")
    mock_min_max.get.return_value = ["mock_min_value", "mock_max_value"]
    mocker.patch("main.utils.is_syntax_valid", return_value=True)
    mocker.patch("main.utils.values_are_in_range", return_value=False)

    with pytest.raises(ValueError) as e:
        main()
    expcted_error = "Argument for `mock_args` has invalid value!"

    assert str(e.value) == expcted_error


def test_main_success(mocker):
    mocker.patch.object(sys, "argv", ["script", "foo bar baz x y command"])
    mock_arg = mocker.Mock()
    mock_arg.value = "mock_args"
    mocker.patch.object(const, "ORDER_OF_ARGS", side_effect=mock_arg)
    mock_min_max = mocker.patch("main.const.ARGS_MIN_AND_MAX_VALUES")
    mock_min_max.get.return_value = ["mock_min_value", "mock_max_value"]
    mocker.patch("main.utils.is_syntax_valid", return_value=True)
    mocker.patch("main.utils.values_are_in_range", return_value=True)
    mock_proccess_expression = mocker.patch("main.utils.process_expression")
    mock_proccess_expression.side_effect = ["a", "b", "c", "d", "e"]

    actual_output = main()
    expected_output = (
        f"{'minute'.ljust(14)}a\n"
        f"{'hour'.ljust(14)}b\n"
        f"{'day of month'.ljust(14)}c\n"
        f"{'month'.ljust(14)}d\n"
        f"{'day of week'.ljust(14)}e\n"
        f"{'command'.ljust(14)}command"
    )

    assert actual_output == expected_output
