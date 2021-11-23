#Практическое занятие №7_Задача №2.
class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_expense_coat(self):
        return self.size / 6.5 + 0.5

    def get_expense_costume(self):
        return self.height * 2 + 0.3

    @property
    def get_exp_full(self):
        return str(f'Общий расход ткани \n'
                   f' {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')

class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.expense_coat = round(self.size / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Расход ткани на пальто {self.expense_coat}'

class Costume(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.expense_costume = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Расход ткани на костюм {self.expense_costume}'

coat = Coat(2, 0)
costume = Costume(0, 3)
clothes = Clothes(2, 3)
print(coat)
print(costume)
print(clothes.get_exp_full)