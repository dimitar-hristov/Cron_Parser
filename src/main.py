import sys

from utils import const, utils


def main() -> str:
    # If no argument is provided or there is a missing element, print a help message
    if len(sys.argv) == 2 and len(sys.argv[1].split(" ")) == 6:
        cron_expression = sys.argv[1].split(" ")
        output = []
        for i in range(5):
            expression = cron_expression[i].strip()
            min_value = const.ARGS_MIN_AND_MAX_VALUES.get(const.ORDER_OF_ARGS[i])[0]
            max_value = const.ARGS_MIN_AND_MAX_VALUES.get(const.ORDER_OF_ARGS[i])[1]

            if utils.is_syntax_valid(
                expression=expression
            ) and utils.values_are_in_range(
                expression=expression, min_value=min_value, max_value=max_value
            ):
                output.append(
                    utils.process_expression(
                        expression=expression,
                        min_value=min_value,
                        max_value=max_value,
                    )
                )
            else:
                raise ValueError(
                    f"Argument for `{str(const.ORDER_OF_ARGS[i].value)}` has invalid value!"
                )
        # add the command at the end
        output.append(cron_expression[5].strip())

        return (
            f"{'minute'.ljust(14)}{output[0]}\n"
            f"{'hour'.ljust(14)}{output[1]}\n"
            f"{'day of month'.ljust(14)}{output[2]}\n"
            f"{'month'.ljust(14)}{output[3]}\n"
            f"{'day of week'.ljust(14)}{output[4]}\n"
            f"{'command'.ljust(14)}{output[5]}"
        )
    else:
        return (
            "Cron Expression Parser. \n"
            "You need to provide a single string specifying: \n"
            "\t- minutes; \n"
            "\t- hours \n"
            "\t- day of month \n"
            "\t- month \n"
            "\t- day of week; \n"
            "\t- and the command as a cron expression."
        )


if __name__ == "__main__":
    try:
        result = main()
        print(result)
    except Exception as e:
        print(e)
