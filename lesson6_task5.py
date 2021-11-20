# Практическое задание 6_Задача №5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью ручки: {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью карандаша: {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью маркера: {self.title}")

pen = Pen("Мир")
pencil = Pencil("Труд")
handle = Handle("Май")
for s in (pen, pencil, handle):
    s.draw()
