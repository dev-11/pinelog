from logging import log


@log
def method(a, b):
    a = 1 / 0
    return "Hello World!"


if __name__ == "__main__":
    method(1, {"a": 1})
