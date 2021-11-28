# Практическое задание №8_Задача №3:
class CheckForNumeric(ValueError):
    pass

my_list = []
while True:
    try:
        value = input('Введите значение, затем нажмите Enter: ')
        if value == 'stop':#Стоп сигнал для окончания ввода данных списка
            break
        if not value.isdigit():
            raise CheckForNumeric(value)
        my_list.append(int(value))
    except CheckForNumeric as ex:
        print('Это не число!', ex)
print(my_list)