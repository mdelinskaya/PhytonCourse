#Урок 3_Задание 2.

def my_description (first_name, second_name, year_of_birth, city, e_mail, telephone):
    return first_name + ' ' + second_name + ', гг.р: ' + year_of_birth + ', город ' + city + ', e-mail: ' + e_mail + ', тел: ' + telephone
print(my_description(city = input('Укажите город вашего проживания: '), year_of_birth = input('Укажите ваш год рождения: '), e_mail = input('Укажите ваш e-mail: '), telephone = input('Укажите ваш телефон: '), first_name = input('Укажите ваше имя: '), second_name = input('Укажите вашу фамилию: ')))
