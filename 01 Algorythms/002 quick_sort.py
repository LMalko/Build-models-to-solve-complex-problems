from time_it import time_it_for_recursive
import random


@time_it_for_recursive
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


# Slicker alternative, but much slower.

# @time_it_for_recursive
# def quick_sort(collection):
#     if len(collection) < 1:
#         return collection
#
#     less = quick_sort([element for element in collection if element < collection[0]])
#     equal = [element for element in collection if element == collection[0]]
#     greater = quick_sort([element for element in collection if element > collection[0]])
#
#     return  less + equal + greater
# small_list = [1,]
# big_list = [1,]