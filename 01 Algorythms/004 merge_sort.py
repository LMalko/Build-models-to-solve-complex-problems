import random
import sys
sys.path.append("..")
from resources.time_it import time_it_for_recursive

@time_it_for_recursive
def merge_sort(collection):
    print ( "Splitting ", collection )
    if len(collection)>1:
        mid = len(collection) // 2
        lefthalf = collection[:mid]
        righthalf = collection[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        left_index = 0
        right_index = 0
        collection_index = 0
        print("debug", left_index, right_index, collection_index, lefthalf, righthalf, collection)
        while left_index < len(lefthalf) and right_index < len(righthalf):
            if lefthalf[left_index] < righthalf[right_index]:
                collection[collection_index] = lefthalf[left_index]
                left_index += 1
            else:
                collection[collection_index] = righthalf[right_index]
                right_index += 1
            collection_index += 1

        while left_index < len(lefthalf):
            collection[collection_index] = lefthalf[left_index]
            left_index += 1
            collection_index += 1

        while right_index < len(righthalf):
            collection[collection_index] = righthalf[right_index]
            right_index += 1
            collection_index += 1
    print("Merging ", collection)
    return collection

small_list = [50,]
big_list = [4,]


while(len(small_list) < 6):
    number = random.randint(1, 101)
    small_list.append(number)

while(len(big_list) < 50000):
    number = random.randint(1, 50001)
    big_list.append(number)

print(small_list)
small_list = merge_sort(small_list)
big_list = merge_sort(big_list)
print(small_list)
print(big_list)