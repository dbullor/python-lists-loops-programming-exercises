#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
for n in range(0,10):
    my_number= random.randint(0,10)
    my_list.append(my_number)
print(my_list)
