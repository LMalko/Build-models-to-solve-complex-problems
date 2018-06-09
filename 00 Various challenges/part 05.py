# 01 Calculate array of numbers(with possible repetitions) permutations, max and min.

from operator import mul
from math import factorial
from functools import reduce
from collections import Counter

def proc_arr(arr):
    s = ''.join(sorted(arr))
    # print("-" * 20)
    # print(factorial(len(arr)))
    # print(Counter(arr))
    # print(Counter(arr).values())
    # print(list(map(factorial, Counter(arr).values())))
    # print(reduce(mul, map(factorial, Counter(arr).values())))
    return [factorial(len(arr)) // reduce(mul, map(factorial, Counter(arr).values())),
                                                                int(s), int(s[::-1])]

print(proc_arr(['1','2','3','0','5','1','1','3']))