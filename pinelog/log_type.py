from enum import Enum


class LogType(Enum):
    Undefined = 1
    Invoke = 2
    Leave = 3
    Exception = 4
