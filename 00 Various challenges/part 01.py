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


# 05. Find which number is missing from range using sequences.

def find_missing(collection):
    return (max(collection ) + 1) * max(collection) / 2 - sum(collection)

# 06. Check if a number is a sqrt.

def is_square(n):
    if str((n ** 0.5)).split(".")[1] == "0":
        return True
    return False

print(is_square(24))

# 07. Return first pair of numbers in list that sum to the number in parameter

def sum_pairs(list_of_ints, number):
      already_visited = set()
      for i in list_of_ints:
          difference = number - i
          if difference in already_visited:
              return [difference, i]
          already_visited.add(i)
      return []