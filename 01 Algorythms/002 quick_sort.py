from time_it import time_it
import random


@time_it
def quick_sort(collection):
    less = []
    equal = []
    greater = []

    if len(collection) > 1:
        pivot = collection[0]
        for element in collection:
            if element < pivot:
                less.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return collection


small_list = [1,]
big_list = [1,]

while(len(small_list) < 100):
    number = random.randint(1, 101)
    small_list.append(number)

while(len(big_list) < 50000):
    number = random.randint(1, 50001)
    big_list.append(number)

print(quick_sort(small_list))
print(quick_sort(big_list))