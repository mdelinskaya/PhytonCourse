#Урок 4 Задание 7.
def fact(n):
    current = 1
    for el in range(1, n + 1):
        current *= el
        yield current

n = int(input('Укажите целое не отрицательное число n: '))
for el in fact(n):
    print(el)