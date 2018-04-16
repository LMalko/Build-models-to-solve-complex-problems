from time_it import time_it
import random

@time_it
def bubble_sort(collection):
    swapped = False

    while not swapped:

        swapped = True
        for i in range(len(collection ) - 1):
            if collection[i] > collection[i + 1]:
                swapped = False
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
    return collection

small_list = [1,]
big_list = [1,]

while(len(small_list) < 100):
    number = random.randint(1, 101)
    small_list.append(number)

while(len(big_list) < 50000):
    number = random.randint(1, 50001)
    big_list.append(number)

print(bubble_sort(small_list))
print(bubble_sort(big_list))    #will take ages or crash.
