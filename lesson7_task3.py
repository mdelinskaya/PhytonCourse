#Практическое занятие №7_Задача №3.
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, quantity2):
        print('результат сложения: ')
        return Cell(self.quantity + quantity2.quantity)

    def __sub__(self, quantity3):
        print('результат вычитания: ')
        return Cell(self.quantity - quantity3.quantity) if (self.quantity - quantity3.quantity) > 0 else print('Разность меньше нуля!')

    def __mul__(self, quantity4):
        print('результат умножения: ')
        return Cell(self.quantity * quantity4.quantity)

    def __truediv__(self, quantity5):
        print('результат деления: ')
        return Cell(round(self.quantity // quantity5.quantity))

    def __str__(self):
        return self.quantity * "*"

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(20)
cells2 = Cell(5)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 / cells2)
print(cells1 * cells2)
print(cells2.make_order(5))
print(cells1.make_order(10))
