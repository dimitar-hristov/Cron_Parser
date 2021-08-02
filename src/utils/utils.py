import re

def process_expression(expression: str, min_value: int, max_value: int) -> str:
    # *
    if re.search(r"^\*$", expression):
        output_list = [str(minute) for minute in range(min_value, max_value+1)]
        output = " ".join(output_list).strip()
    # */15
    elif re.search(r"^\*/[0-9]+$", expression):
        interval = int(expression.split("/")[1])
        output_list = [str(minute) for minute in range(min_value, max_value+1, interval)]
        output = " ".join(output_list).strip()
    # 1-10
    elif re.search(r"^[0-9]+-[0-9]+$", expression):
        start = int(expression.split("-")[0])
        end = int(expression.split("-")[1])
        output_list = [str(minute) for minute in range(start, end+1)]
        output = " ".join(output_list).strip()
    # 1,2,3,4,5,25
    elif re.search(r"^[0-9]+(,[0-9]+)*$", expression):
        output = " ".join(expression.split(","))
    # 20
    else:
        output = expression

    return output

def is_syntax_valid(expression: str):
    regular_expressions = [
        r"^\*$",                # *             
        r"^\*/[0-9]+$",         # */15        
        r"^[0-9]+-[0-9]+$",     # 1-10        
        r"^[0-9]+(,[0-9]+)*$",  # 1,2,3,4,5,25
        r"^[0-9]+$"             # 20          
    ]
    for regex in regular_expressions:
        if re.search(regex, expression):
            return True
    
    return False

def values_are_in_range(expression: str, min_value: int, max_value: int):
    # *
    if re.search(r"^\*$", expression):
        return True
    # */15
    elif re.search(r"^\*/[0-9]+$", expression):
        value = expression.split("/")[1]
        if int(value) < min_value or int(value) > max_value:
            return False
    # 1-10
    elif re.search(r"^[0-9]+-[0-9]+$", expression):
        values = expression.split("-")
        for value in values:
            if int(value) < min_value or int(value) > max_value:
                return False
    # 1,2,3,4,5,25
    elif re.search(r"^[0-9]+(,[0-9]+)*$", expression):
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
