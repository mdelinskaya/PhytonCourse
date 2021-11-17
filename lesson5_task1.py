#Практическое занятие 5_Задача №1.

with open(‘test.txt’, ‘w’) as file:
    input_line = line(‘Text :\n’)
    while input_line:
        file.write(f’{input_line}\n’)
        input_line = input(‘Text :\n’)
