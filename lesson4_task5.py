#Урок 4 Задание 5.
from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
prod = reduce(lambda x, y: x*y, my_list)
print(prod)