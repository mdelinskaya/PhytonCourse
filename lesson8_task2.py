#Практическое задание №8_Задача №2:

class DivisionByZero:
    def __init__(self, divident, divider):
        self.divident = divident
        self.divider = divider

    @staticmethod
    def divide_by_null(divident, divider):
        try:
            return (divident / divider)
        except:
            return (f"На ноль делить нельзя!")

div = DivisionByZero(1, 2)
print(DivisionByZero.divide_by_null(1, 0))
print(DivisionByZero.divide_by_null(2, 0.1))
print(div.divide_by_null(17, 0))