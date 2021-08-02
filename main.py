import sys
from expression_type import ExpressionType

months = {"JAN": 1, "FEB": 2, "MAR": 3,"APR": 4,"MAY": 5,"JUN": 6,"JUL": 7,"AUG": 8,"SEP": 9,"OCT": 10,"NOV": 11,"DEC": 12}

def process_time(time_expression: str, is_minutes: bool) -> str:
    # Inputs:
    #   *
    #   */15
    #   1-10
    #   1,2,3,4,5,25
    #   20

    if is_minutes:
        max_value = 60
    else:
        max_value = 24

    if time_expression == "*":
        output_time_list = [str(minute) for minute in range(max_value)]
        output_time = " ".join(output_time_list).strip()
    elif "*/" in time_expression:
        interval = int(time_expression.split("/")[1])
        output_time_list = [str(minute) for minute in range(0, max_value, interval)]
        output_time = " ".join(output_time_list).strip()
    elif "-" in time_expression:
        start = int(time_expression.split("-")[0])
        end = int(time_expression.split("-")[1])
        output_time_list = [str(minute) for minute in range(start, end+1)]
        output_time = " ".join(output_time_list).strip()
    elif "," in time_expression:
        output_time = time_expression
    else:
        output_time = time_expression

    return output_time

def process_date(date_expression: str, type: ExpressionType) -> str:
    # Inputs:
    #   *
    #   */15
    #   1-10
    #   1,2,3,4,5,25
    #   20

    if type is ExpressionType.MINUTES:
        min_value = 0
        max_value = 60
    elif type is ExpressionType.HOURS:
        min_value = 0
        max_value = 24
    elif type == ExpressionType.DAY_OF_MONTH:
        min_value = 1
        max_value = 32
    elif type == ExpressionType.MONTH:
        min_value = 1
        max_value = 13
    elif type == ExpressionType.DAY_OF_WEEK:
        min_value = 0
        max_value = 7

    if date_expression == "*":
        output_date_list = [str(minute) for minute in range(min_value, max_value)]
        output_date = " ".join(output_date_list).strip()
    elif "*/" in date_expression:
        interval = int(date_expression.split("/")[1])
        output_date_list = [str(minute) for minute in range(min_value, max_value, interval)]
        output_date = " ".join(output_date_list).strip()
    elif "-" in date_expression:
        start = int(date_expression.split("-")[0])
        end = int(date_expression.split("-")[1])
        output_date_list = [str(minute) for minute in range(start, end+1)]
        output_date = " ".join(output_date_list).strip()
    elif "," in date_expression:
        output_date = date_expression
    else:
        output_date = date_expression

    return output_date

cron_expression = sys.argv[1].split(" ")

minutes_expression = cron_expression[0].strip()
output_minutes = process_date(date_expression=minutes_expression, type=ExpressionType.MINUTES)

hours_expression = cron_expression[1].strip()
output_hours = process_date(date_expression=hours_expression, type=ExpressionType.HOURS)

day_of_moth_expression = cron_expression[2].strip()
output_day_of_month = process_date(date_expression=day_of_moth_expression, type=ExpressionType.DAY_OF_MONTH)

month_expression = cron_expression[3].strip()
output_month = process_date(date_expression=month_expression, type=ExpressionType.MONTH)

day_of_week_expression = cron_expression[4].strip()
output_day_of_week = process_date(date_expression=day_of_week_expression, type=ExpressionType.DAY_OF_WEEK)

print(f"{'minute'.ljust(14)}{output_minutes}")
print(f"{'hour'.ljust(14)}{output_hours}")
print(f"{'day of month'.ljust(14)}{output_day_of_month}")
print(f"{'month'.ljust(14)}{output_month}")
print(f"{'day of week'.ljust(14)}{output_day_of_week}")
print(f"{'command'.ljust(14)}{cron_expression[5].strip()}")
