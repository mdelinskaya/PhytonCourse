#Практическое задание 6_Задача №2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self, spec_grav, thick):
        return self._length * self._width * spec_grav * thick / 1000

r = Road(500, 20)
print(r.get_weight(25, 5))