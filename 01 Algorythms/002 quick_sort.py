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

print(quick_sort([14, 17, 13, 15, 19, 10, 3, 16, 9, 12]))
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

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       print(alist)
       splitpoint = partition(alist,first,last)

       print(alist[splitpoint])
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):

    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark

alist = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
quickSort(alist)
print(alist)
