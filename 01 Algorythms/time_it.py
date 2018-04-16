import time


def time_it(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, *kwargs)
        end = time.time()
        print(function.__name__ + " took " + str((end - start) * 1000) + " mil sec")
        return result
    return wrapper