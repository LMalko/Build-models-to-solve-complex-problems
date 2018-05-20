import sys
sys.path.append("..")
from resources.time_it import time_it_for_recursive
import random


@time_it_for_recursive
def quick_sort(collection):
    less = []
    equal = []
    greater = []

    print(collection)
    if len(collection) > 1:
        # pivot = collection[0]
        # Use median of three
        pivot = sorted([collection[0], collection[-1], collection[round(len(collection)/2)]])[1]
        for element in collection:
            if element < pivot:
                less.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)
        print("dupa", less + equal + greater)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return collection



small_list = [1,]
big_list = [1,]


while(len(small_list) < 10):
    number = random.randint(1, 101)
    small_list.append(number)

while(len(big_list) < 50000):
    number = random.randint(1, 50001)
    big_list.append(number)

# print(quick_sort(small_list))
# print(quick_sort(big_list))


# 2. Slicker alternative, but much slower.

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


# 3. Version with partition
@time_it_for_recursive
def quickSort(collection):
    quickSortHelper(collection, 0, len(collection) - 1)

def quickSortHelper(collection, first_index, last_index):

    if first_index < last_index:
        splitpoint = partition(collection, first_index, last_index)

        quickSortHelper(collection, first_index, splitpoint - 1)
        quickSortHelper(collection, splitpoint + 1, last_index)

def partition(collection, first_index, last_index):

    pivot_value = collection[first_index]
    left_mark = first_index + 1
    right_mark = last_index

    done = False
    while not done:

        while left_mark <= right_mark and collection[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while collection[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            collection[left_mark], collection[right_mark] = collection[right_mark], collection[left_mark]


    collection[first_index], collection[right_mark] = collection[right_mark], collection[first_index]
    return right_mark

collection = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
quickSort(collection)
print(collection)

# quick_sort(big_list)
# print(big_list)
