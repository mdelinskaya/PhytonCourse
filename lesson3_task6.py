# Урок 3_Задание 6.
def int_func(string1):
    cap_string = string1.capitalize()
    return cap_string
print(int_func(input('Латинское слово маленькими буквами: ')))
string2 = input('Введите строку из слов по латински, разделенную пробелами: ')
list1 = string2.split()
for i in range(len(list1)):
    list1[i] = int_func(list1[i])
print(' '.join(list1))