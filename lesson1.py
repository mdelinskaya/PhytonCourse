#Урок 1.

# Задание 1.
num_1 = int(input('Введите первую переменную: '))
num_2 = int(input('Введите вторую переменную: '))
res_nums_1 = num_1 + num_2
res_nums_2 = num_1/num_2
res_nums_3 = num_1//num_2
res_nums_4 = num_1%num_2
res_nums_5 = (num_1 > num_2) and (num_2 > 1)
print(res_nums_1, ',', res_nums_2, ',', res_nums_3, ',', res_nums_4, ',', res_nums_5)
num_str_1 = input('Введите первый фрагмент текста: ')
num_str_2 = input('Введите второй фрагмент текста: ')
res_str = num_str_1 + ' ' + num_str_2
print(res_str)

# Задание 2.
time_in_sec = int(input('Введите время в секундах: '))
hour_res = time_in_sec//3600
min_in_sec = time_in_sec - hour_res*3600
min_res = min_in_sec//60
sec_res = min_in_sec - min_res*60
print(hour_res, ':', min_res, ':', sec_res)

# Задание 3.
num_str = input('Введите любое число от 1 до 9: ')
first_num = int(num_str)
second_num_str = num_str*2
second_num = int(second_num_str)
third_num_str = num_str*3
third_num = int(third_num_str)
res_num = first_num + second_num + third_num
print (res_num)

# Задание 4.
num = int(input('Введите любое положительное число: '))
rest_1 = num % 10
biggest = rest_1
num = num//10
while num > 0:
    rest_2 = num % 10
    if rest_2 > biggest:
        biggest = rest_2
    num = num//10
result_str = f'Самая большая цифра в данном числе - {biggest}'
print(result_str)

# Задание 5.
proceeds = int(input('Укажите выручку компании за год в рублях: '))
costs = int(input('Укажите издержки компании за год в рублях: '))
if proceeds > costs:
    profit = proceeds - costs
    profitability = profit/proceeds*100
    profitability_round = round(profitability, 2)
    print('В этом году компания получила прибыль')
    print('Рентабельность выручки', profitability_round,'%')
    employees = int(input('Укажите число сотрудников в компании: '))
    profit_for_employees_rub = profit//employees
    profit_for_employees_kop = profit%employees
    profit_for_employees_kop_round = round(profit_for_employees_kop, 2)
    print('Прибыль на каждого сотрудника компании ', profit_for_employees_rub, 'руб.', profit_for_employees_kop_round, 'коп.' )
else:
    print('В этом году компания понесла убытки')

# Задание 6.
initial_km = int(input('Укажите количество километров, которое спортсмен пробежл в первый день: '))
target_km = int(input('Укажите целевое количество километров, котрое спортсмен должен пробегать в итоге: '))
day_number = 1
if target_km == initial_km:
    result_day_str = f'Целевого количества километров спортсмен достигнет через {day_number} дней'
    print(result_day_str)
else:
   while target_km > initial_km:
      initial_km = initial_km + initial_km/100*10
      day_number += 1
      result_day_str = f'Целевого количества километров спортсмен достигнет через {day_number} дней'
   print(result_day_str)
