#Урок 3_Задание 3.
def greatest_sum (arg_1, arg_2, arg_3):
    list1 = (arg_1, arg_2, arg_3)
    sort_list = sorted(list1)
    if sort_list[1] > sort_list[0]:
         a = sort_list[1] + sort_list[2]
         return a
    else:
         b = ('Невозможно определить 2 наибольших числа')
         return b
print(greatest_sum(arg_1 = int(input('Введите первое число: ')), arg_2 = int(input('Введите второе число: ')), arg_3 = int(input('Введите третье число: '))))