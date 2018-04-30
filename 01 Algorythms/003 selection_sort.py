import copy
import random
import sys
sys.path.append("..")
from resources.time_it import time_it

@time_it
def selection_sort(collection):
    start = 0

    for i in range(len(collection)):
        minimum = collection[start]
        swapped = False
        while not swapped:
            swapped = True
            for index, value in enumerate(collection[start:]):
                if value < minimum:
                    swapped = False
                    temp_index = index
                    minimum = value
            if not swapped:
                collection[temp_index + start], collection[start] = collection[start], minimum
        start += 1
    return collection

small_list = [40,]
big_list = [40,]


while(len(small_list) < 100):
    number = random.randint(1, 101)
    small_list.append(number)

while(len(big_list) < 50000):
    number = random.randint(1, 50001)
    big_list.append(number)

print(selection_sort(small_list))
# print(selection_sort(big_list))

