import time


def time_it(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, *kwargs)
        end = time.time()
        time_in_milsec = (end - start) * 1000
        print("{} took {} mil sec.".format(function.__name__, str(time_in_milsec)))
        return result
    return wrapper


def time_it_for_recursive(function):
    time_it.total = 0
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, *kwargs)
        end = time.time()
        time_in_milsec = (end - start) * 1000
        print("Latest {} took {} mil sec.".format(function.__name__, str(time_in_milsec)))
        time_it.total += time_in_milsec
        print("Latest total time is {} mil sec".format(str(time_it.total)))
        return result
    return wrapper