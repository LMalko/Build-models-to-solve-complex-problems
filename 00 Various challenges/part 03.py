# 01. Exchange chars in string.

print("aei23ou".translate(str.maketrans("aeiou", "uoiea")))

# 02. Filter elements to list under condition.

    # Filter only positive numbers NOT REPEATING:
lista = [-3, -4, -1, 2, -7, 4]
print(list(filter(lambda x: x > 0, lista)))

# 03. Sort under condition without changing elements.

lista = ["a", "C", "b", "a", "c", "A"]
print(sorted(lista, key=lambda x: x.lower(), reverse=True))
    # min(lista, key=lambda number: number * number)
    # max(lista, key=lambda number: number * number)

# 04. Keeping track how many times a function was called.

def running_average():
    running_average.counter = 0
    running_average.total = 0
    def funkcja(number):
        running_average.counter += 1
        running_average.total += number
        return running_average.total / running_average.counter
    return funkcja

    # rAvg = running_average();
    # rAvg(10) // 10.0;
    # rAvg(11) // 10.5;
    # rAvg(12) // 11;
    #
    # rAvg2 = running_average()
    # rAvg2(1) // 1
    # rAvg2(3) // 2

# 05. Allowing function be called only once.

def once(funkcja):
    once.count = 0
    def funkcja(a, b):
        once.count += 1
        if once.count > 1:
            return None
        return a + b
    return funkcja

def add(a,b):
    return a+b

oneAddition = once(add)

print(oneAddition(2,2))
print(oneAddition(2,2))
print(oneAddition(12,200))

# 06. Elements key sorted in ordered of occurence.
from collections import Counter
letters_occurence = Counter("Composition is achieved by using insta76nce variables that refers to other objects.")

letters_in_order_of_frequency = "".join(sorted(letters_occurence.keys(),
                                                   key=lambda x: letters_occurence[x], reverse=True))

print(letters_in_order_of_frequency)

# 07. Count nested lists.

def count_list(lista):
    count = 0
    for e in lista:
        if isinstance(e, list):
            count = count + 1 + count_list(e)
    return count

# 08. Sort numbers in multiple nested lists.

import re
def sort_nested_list(array):
    array_to_string=str(array);

    # Collect all numbers from nested arrays.
    numbers=sorted(re.findall(r"\d+",array_to_string), key=int, reverse=True)


    return re.sub(r"\d+", lambda number: numbers.pop(), array_to_string)


print(sort_nested_list([[[[[[[[[2, 1], [3,4]], [[6, 5], [8, 7]]]]]]]]]))
print(sort_nested_list([[[29, 32], [82, 61], [75, 91]], [[[69, 99], [74, 23], [70, 97]]]]))