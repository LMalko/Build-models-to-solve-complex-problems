from time_it import time_it
import random


@time_it
def insertion_sort(collection):
    for index in range(1, len(collection)):
        currentvalue = collection[index]
        position = index
        while position > 0 and collection[position - 1] > currentvalue:
            collection[position] = collection[position - 1]
            position = position - 1
        collection[position] = currentvalue
    return collection

small_list = [1,]
big_list = [1,]

while(len(small_list) < 100):
    number = random.randint(1, 101)
    small_list.append(number)

while(len(big_list) < 5000):
    number = random.randint(1, 5001)
    big_list.append(number)

print(insertion_sort(small_list))
print(insertion_sort(big_list))