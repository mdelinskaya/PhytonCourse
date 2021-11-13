#Урок 4 Задание 2.
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
length = len(my_list)
new_list = [my_list[el] for el in range(1, length) if my_list[el] > my_list[el-1]]
print(new_list)