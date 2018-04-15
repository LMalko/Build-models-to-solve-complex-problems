# 01. Create a dictionary out of list1(keys) & list2(values).

def two_list_dictionary(a,b):
    return {**{}.fromkeys(a, "EMPTY"), **dict(zip(a,b))}

print(two_list_dictionary(["a", "b", "c", "d", "e"], [1,2,3,4]))

# 02. Create dictionary out of string letters occurence.

from collections import Counter

def strings_construction(string):
    return dict(Counter(string))

print(strings_construction("This is a test string, You can put anything here."))

# 03. Check the length of the longest string.

def check_for_longest(collection):
    return len(max(collection, key=len))

print(check_for_longest(["aaaaaaa", "bb", "cccccccc", "ddddddddddddd", "eeee"]))

# 04. Nearest square number.

def nearest_square_number(number):
    return round(number ** 0.5) ** 2

print(nearest_square_number(37))