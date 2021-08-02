import sys
from expression_type import ExpressionType
import re

months = {"JAN": 1, "FEB": 2, "MAR": 3,"APR": 4,"MAY": 5,"JUN": 6,"JUL": 7,"AUG": 8,"SEP": 9,"OCT": 10,"NOV": 11,"DEC": 12}
order_of_args = [ExpressionType.MINUTES, ExpressionType.HOURS, ExpressionType.DAY_OF_MONTH, ExpressionType.MONTH, ExpressionType.DAY_OF_WEEK]
args_min_and_max_values = {
    ExpressionType.MINUTES: (0, 59), 
    ExpressionType.HOURS: (0, 23), 
    ExpressionType.DAY_OF_MONTH: (1, 31), 
    ExpressionType.MONTH: (1, 12), 
    ExpressionType.DAY_OF_WEEK: (0, 6)
}

def process_expression(expression: str, min_value: int, max_value: int) -> str:
    # *
    if re.search("^\*$", expression):
        output_date_list = [str(minute) for minute in range(min_value, max_value+1)]
        output_date = " ".join(output_date_list).strip()
    # */15
    elif re.search("^\*\/[0-9][0-9]?$", expression):
        interval = int(expression.split("/")[1])
        output_date_list = [str(minute) for minute in range(min_value, max_value+1, interval)]
        output_date = " ".join(output_date_list).strip()
    # 1-10
    elif re.search("^[0-9]-[0-9]$", expression):
        start = int(expression.split("-")[0])
        end = int(expression.split("-")[1])
        output_date_list = [str(minute) for minute in range(start, end+1)]
        output_date = " ".join(output_date_list).strip()
    # 1,2,3,4,5,25
    # 20
    else:
        output_date = expression

    return output_date

def is_syntax_valid(expression: str):
    regular_expressions = [
        "^\*$",                 # *             
        "^\*\/[0-9][0-9]?$",    # */15        
        "^[0-9]-[0-9]$",        # 1-10        
        "^[0-9](,[0-9]+)*$",    # 1,2,3,4,5,25
        "^[0-9]+$"              # 20          
    ]
    for regex in regular_expressions:
        if re.search(regex, expression):
            return True
    
    return False

def values_are_in_range(expression: str, min_value: int, max_value: int):
    # *
    if re.search("^\*$", expression):
        return True
    # */15
    elif re.search("^\*\/[0-9][0-9]?$", expression):
        value = expression.split("/")[1]
        if int(value) < min_value or int(value) > max_value:
            return False
    # 1-10
    elif re.search("^[0-9]-[0-9]$", expression):
        values = expression.split("-")
        for value in values:
            if int(value) < min_value or int(value) > max_value:
                return False
    # 1,2,3,4,5,25
    elif re.search("^[0-9](,[0-9]+)*$", expression):
        values = expression.split(",")
        for value in values:
            if int(value) < min_value or int(value) > max_value:
                return False
    # 20 
    else:
        value = int(expression)
        if value < min_value or value > max_value:
            return False
    
    return True
    


cron_expression = sys.argv[1].split(" ")

if len(cron_expression) == 6:
    output = []
    for i in range(5):
        expression = cron_expression[i].strip()
        min_value = args_min_and_max_values.get(order_of_args[i])[0]
        max_value = args_min_and_max_values.get(order_of_args[i])[1]
        
        if is_syntax_valid(expression=expression) and values_are_in_range(expression=expression, min_value=min_value, max_value=max_value):
            output.append(process_expression(expression=expression, min_value=min_value, max_value=max_value))
        else:
            raise ValueError(f"Argument for `{str(order_of_args[i].value)}` has invalid value!")
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
