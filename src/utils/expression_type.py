from enum import Enum


class ExpressionType(Enum):
    MINUTES = "minutes"
    HOURS = "hours"
    DAY_OF_MONTH = "day of month"
    MONTH = "month"
    DAY_OF_WEEK = "day of week"
