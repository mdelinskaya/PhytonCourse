#Урок 2.

# Задание 1.
my_list = [7, 5.2, 8, 'Text', True, False, 'Text2']
length = len(my_list)
elem = 0
while length > elem:
    print(type(my_list[elem]))
    elem += 1    
    
# Задание 2.
my_list2 = []
el_number = int(input('Укажите количество элементов списка: '))
couples_number = el_number // 2
if el_number == 0:
    print('В списке 0 элементов')
elif el_number == 1:
    el = input('Укажите единственный элемент списка: ')
    my_list2.append(el)
else:
    el = input('Укажите первый элемент списка: ')
    my_list2.append(el)
    step = 1
    while step < el_number:
        el = input('Укажите следующий элемент списка: ')
        my_list2.append(el)
        step += 1
print('Исходный список: ', my_list2)
a = 0
step2 = 0
while step2 < couples_number:
    container = my_list2[a]
    my_list2[a] = my_list2[a+1]
    my_list2[a+1] = container
    a += 2
    step2 += 1
print('Список после перестановок: ', my_list2)

# Задание 3.

month_number = int(input('Укажите номер месяца в году (от 1 до 12): '))
season = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
print('Указанный месяц относится к сезону', season.get(month_number))

# Задание 4.
user_string = input('Введите строку из нескольких слов, разделенных пробелами: ')
user_string_list = user_string.split()
for el in range(len(user_string_list)):
    user_str = user_string_list[el]
    user_str10 = user_str[:10]
    user_string_list[el] = user_str10
for el in enumerate(user_string_list):
    print(el)
    
# Задание 5.
print('Задан следующий набор чисел: 7, 5, 3, 3, 2')
my_rating = [7, 5, 3, 3, 2]
user_rat_el = int(input('Введите новый элемент рейтинга: '))
i = 0
while i < len(my_rating):
    a = my_rating[i]
    if user_rat_el >= a:
        position = i
        break
    else:
        i += 1
my_rating.insert(i, user_rat_el)
print(my_rating)

# Задание 6.
print('В этой задаче необходимо ввести параметры для трех товаров')
prod1_name = input('Введите название первого товара: ')
prod1_price = int(input('Укажите цену первого товара: '))
prod1_number = int(input('Укажите количество первого товара: '))
prod1_unit = input('Укажите единицу измерения первого товара: ')
prod2_name = input('Введите название второго товара: ')
prod2_price = int(input('Укажите цену второго товара: '))
prod2_number = int(input('Укажите количество второго товара: '))
prod2_unit = input('Укажите единицу измерения второго товара: ')
prod3_name = input('Введите название третьего товара: ')
prod3_price = int(input('Укажите цену третьего товара: '))
prod3_number = int(input('Укажите количество третьего товара: '))
prod3_unit = input('Укажите единицу измерения третьего товара: ')
my_dict_1 = {'название': prod1_name, 'цена': prod1_price, 'количество': prod1_number, 'ед': prod1_unit}
my_dict_2 = {'название': prod2_name, 'цена': prod2_price, 'количество': prod2_number, 'ед': prod2_unit}
my_dict_3 = {'название': prod3_name, 'цена': prod3_price, 'количество': prod3_number, 'ед': prod3_unit}
tuple1 = (1, my_dict_1)
tuple2 = (2, my_dict_2)
tuple3 = (3, my_dict_3)
my_list = [tuple1, tuple2, tuple3]
#Аналитика
analytics = {'название': [prod1_name, prod2_name, prod3_name], 'цена': [prod1_price, prod2_price, prod3_price], 'количество': [prod1_number, prod2_number, prod3_number], 'ед': [prod1_unit, prod2_unit, prod3_unit]}
print(analytics)