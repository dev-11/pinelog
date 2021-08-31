import pinelog

@pinelog.log
def method(*args, **kwargs):
    return kwargs

if __name__ == "__main__":
    method(1,2,3,4,5, {'a':True})
