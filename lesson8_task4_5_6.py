# Практическое задание №8_Задачи 4, 5 и 6:
class SkladOrgtech:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

class Equipment:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.price} {self.year}'

class Printer(Equipment):
    def __init__(self, series, name, price, year):
        super().__init__(name, price, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.price} {self.year}'

class Scaner(Equipment):
    def __init__(self, name, price, year):
        super().__init__(name, price, year)

class Copier(Equipment):
    def __init__(self, name, price, year, refueled): # refueled - признак того, что картридж заполняемый, а не сменный, булевое значение)
        super().__init__(name, price, year)
        self.refueled = refueled
    def __repr__(self):
        return f'{self.name} {self.price} {self.year} {self.refueled}'

sklad = SkladOrgtech()
scaner = Scaner('hp', 1200, 1999)
sklad.add_to(scaner)
scaner = Scaner('hp', 1500, 2010)
sklad.add_to(scaner)
printer = Printer('sony', '14-47s', 2410, 2018)
sklad.add_to(printer)
copier = Copier('xerox', 3000, 2018, True)
sklad.add_to(copier)
print(sklad._dict)
