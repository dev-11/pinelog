from .log_entry import LogEntry
from .log_level import LogLevel
from .log_type import LogType
from .constants import PayloadKeys


def build_invocation_log_entry(class_name, method_name, args):
    return LogEntry(
        LogLevel.Information,
        LogType.Invoke,
        {
            PayloadKeys.ClassNameKey: class_name,
            PayloadKeys.MethodKey: method_name,
            PayloadKeys.ArgsKey: args,
        },
    )


def build_leave_log_entry(class_name, method_name, return_value):
    return LogEntry(
        LogLevel.Information,
        LogType.Leave,
        {
            PayloadKeys.ClassNameKey: class_name,
            PayloadKeys.MethodKey: method_name,
            PayloadKeys.ReturnValueKey: return_value,
        },
    )


def build_exception_log_entry(class_name, method_name, exception):
    return LogEntry(
        LogLevel.Error,
        LogType.Exception,
        {
            PayloadKeys.ClassNameKey: class_name,
            PayloadKeys.MethodKey: method_name,
            PayloadKeys.ExceptionKey: exception,
        },
    )
