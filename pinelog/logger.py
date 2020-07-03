import traceback

from .log_entry_builder import (
    build_invocation_log_entry,
    build_leave_log_entry,
    build_exception_log_entry,
)


def log(f):
    def inner(*args):
        try:
            print(build_invocation_log_entry("class_name1", f.__name__, args))
            result = f(*args)
            print(build_leave_log_entry("class_name1", f.__name__, result))
            return result
        except Exception:
            print(
                build_exception_log_entry(
                    "class_name1", f.__name__, traceback.format_exc()
                )
            )
            raise

    return inner
