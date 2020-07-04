import traceback
import functools
from datetime import datetime as dt
from .log_entry import LogEntry

from .log_entry_builder import (
    build_invocation_log_entry,
    build_leave_log_entry,
    build_exception_log_entry,
)


def log(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        try:
            full_name = f.__qualname__
            class_name = full_name.split('.')[0] if '.' in full_name else None

            _log(build_invocation_log_entry(class_name, f.__name__, args))
            result = f(*args, **kwargs)
            _log(build_leave_log_entry(class_name, f.__name__, result))
            return result
        except Exception:
            _log(
                build_exception_log_entry(
                    class_name, f.__name__, traceback.format_exc()
                )
            )
            raise

    return inner


def _log(log_entry: LogEntry):
    print(f'{dt.now().isoformat()}|{log_entry.log_level}|{log_entry.log_type}|{log_entry.payload}')
