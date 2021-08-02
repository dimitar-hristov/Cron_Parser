import sys

from utils.const import ARGS_MIN_AND_MAX_VALUES, ORDER_OF_ARGS
from utils.expression_type import ExpressionType
from utils.utils import (is_syntax_valid, process_expression,
                         values_are_in_range)

cron_expression = sys.argv[1].split(" ")

if len(cron_expression) == 6:
    output = []
    for i in range(5):
        expression = cron_expression[i].strip()
        min_value = ARGS_MIN_AND_MAX_VALUES.get(ORDER_OF_ARGS[i])[0]
        max_value = ARGS_MIN_AND_MAX_VALUES.get(ORDER_OF_ARGS[i])[1]

        if is_syntax_valid(expression=expression) and values_are_in_range(
            expression=expression, min_value=min_value, max_value=max_value
        ):
            output.append(
                process_expression(
                    expression=expression, min_value=min_value, max_value=max_value
                )
            )
        else:
            raise ValueError(
                f"Argument for `{str(ORDER_OF_ARGS[i].value)}` has invalid value!"
            )
    # add the command at the end
    output.append(cron_expression[5].strip())

    print(f"{'minute'.ljust(14)}{output[0]}")
    print(f"{'hour'.ljust(14)}{output[1]}")
    print(f"{'day of month'.ljust(14)}{output[2]}")
    print(f"{'month'.ljust(14)}{output[3]}")
    print(f"{'day of week'.ljust(14)}{output[4]}")
    print(f"{'command'.ljust(14)}{output[5]}")
else:
    print("Invalid input!")
