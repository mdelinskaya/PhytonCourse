# #Урок 3_Задание 5.
ext_summ = 0
def summ(string1):
    global check, ext_summ
    check = string1.find('$')
    if check == -1:
        list1 = string1.split()
        result1 = [int(item) for item in list1]
        sum_result = sum(result1)
        ext_summ = ext_summ + sum_result
        return ext_summ
    else:
        list2 = string1.split('$',1)[0]
        list3 = list2.split()
        result2 = [int(item) for item in list3]
        sum_result = sum(result2)
        ext_summ = ext_summ + sum_result
        return ext_summ
check = -1
while check == -1:
    print(summ(input('Введите несколько чисел через пробел: ')))

