import sys
sys.path.append("..")
from resources.time_it import time_it
import random

@time_it
def shell_sort(collection):
    print(collection)
    sublist_count = len(collection) // 2
    print(sublist_count)
    while sublist_count > 0:

        for start_position in range(sublist_count):

            gapInsertionSort(collection, start_position, sublist_count)

        print(f"After increments of size {sublist_count} the list is {collection}.")

        sublist_count = sublist_count // 2

def gapInsertionSort(collection, start, gap):
    print(start, gap)
    for i in range(start + gap, len(collection), gap):

        current_value = collection[i]
        position = i

        while position >= gap and collection[position - gap] > current_value:
            collection[position] = collection[position - gap]
            position = position - gap

        collection[position] = current_value


small_list = [1,]
big_list = [1,]


while(len(small_list) < 10):
    number = random.randint(1, 101)
    small_list.append(number)

while(len(big_list) < 50000):
    number = random.randint(1, 50001)
    big_list.append(number)

print(shell_sort(small_list))
# print(shell_sort(big_list))