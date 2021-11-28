# Практическое задание №8_Задача 7:
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, next_z):
        print(f'Сумма z_1 и z_2: ')
        return f'z = {self.a + next_z.a} + {self.b + next_z.b} * i'

    def __mul__(self, next1_z):
        print(f'Произведение z_1 и z_2: ')
        return f'z = {(self.a * next1_z.a) - (self.b * next1_z.b)} + {(self.a * next1_z.b) + (self.b * next1_z.a)} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'

z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print('Первое комплексное число: ', z_1)
print('Второе комплексное число: ', z_2)
print(z_1 + z_2)
print(z_1 * z_2)