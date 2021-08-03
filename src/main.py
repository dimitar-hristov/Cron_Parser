import sys

from utils import utils
from utils.const import ARGS_MIN_AND_MAX_VALUES, ORDER_OF_ARGS

# If no argument is provided or there is a missing element, print a help message
if len(sys.argv) == 2 and len(sys.argv[1].split(" ")) == 6:
    cron_expression = sys.argv[1].split(" ")
    output = []
    for i in range(5):
        expression = cron_expression[i].strip()
        min_value = ARGS_MIN_AND_MAX_VALUES.get(ORDER_OF_ARGS[i])[0]
        max_value = ARGS_MIN_AND_MAX_VALUES.get(ORDER_OF_ARGS[i])[1]

        if utils.is_syntax_valid(expression=expression) and utils.values_are_in_range(
            expression=expression, min_value=min_value, max_value=max_value
        ):
            output.append(
                utils.process_expression(
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
    print("Cron Expression Parser. \n"
        "You need to provide a single string specifying: \n"
        "\t- minutes; \n"
        "\t- hours \n"
        "\t- day of month \n"
        "\t- month \n"
        "\t- day of week; \n"
        "\t- and the command as a cron expression. \n"
    )
