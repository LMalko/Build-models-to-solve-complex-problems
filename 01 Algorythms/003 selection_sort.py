
import random
import sys
sys.path.append("..")
from resources.time_it import time_it

@time_it_for_recursive
def selection_sort(collection):
   pass



small_list = [1,]
big_list = [1,]


while(len(small_list) < 100):
    number = random.randint(1, 101)
    small_list.append(number)

while(len(big_list) < 50000):
    number = random.randint(1, 50001)
    big_list.append(number)

print(selection_sort(small_list))
print(selection_sort(big_list))
