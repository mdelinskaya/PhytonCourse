#Урок 4 Задание 6.
#пункт а.
from itertools import count
print ('Это сгенерированный список: ')
for el in count(3):
    if el > 10:
        break
    else:
        print(el)
#пункт b.
print('А это список, повторяющий заданные значения: ')
my_list = [5, 8, 1, 20, 7, 11]
length = len(my_list)
from itertools import cycle
count = 0
for el in cycle(my_list):
    if count > length * 2:
        break
    print(el)
    count += 1