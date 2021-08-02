from expression_type import ExpressionType

ORDER_OF_ARGS = [
    ExpressionType.MINUTES, 
    ExpressionType.HOURS, 
    ExpressionType.DAY_OF_MONTH, 
    ExpressionType.MONTH, 
    ExpressionType.DAY_OF_WEEK
]

ARGS_MIN_AND_MAX_VALUES = {
    ExpressionType.MINUTES: (0, 59), 
    ExpressionType.HOURS: (0, 23), 
    ExpressionType.DAY_OF_MONTH: (1, 31), 
    ExpressionType.MONTH: (1, 12), 
    ExpressionType.DAY_OF_WEEK: (0, 6)
}