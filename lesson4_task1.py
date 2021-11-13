#Урок 4 Задание 1.
from sys import argv

if len(argv) < 4:
    print (f'Укажте через пробел выработку, ставку и премию')
else:
    work = float(argv[1])
    rate = float(argv[2])
    award = float(argv[3])
    result = work * rate + award
    print(result)
#запускала в терминале вот с таким путем и параметрами: python C:\Users\Dell\PhytonBasics\python_basics\lesson4_task1.py 8 500 10000
# все посчиталось верно - был ответ: 14000.0