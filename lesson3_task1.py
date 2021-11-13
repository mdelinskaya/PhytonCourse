#Урок 3_Задание 1.

def my_func(arg_1, arg_2):
    if arg_2 == 0:
        return ('Деление на ноль невозможно')
    else:
        return arg_1/arg_2
dividend = int(input('Укажите делимое: '))
divider = int(input('Укажите делитель: '))
print(my_func(dividend, divider))


    
