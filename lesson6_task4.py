# Практическое задание 6_Задача №4
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Go')
    def stop(self):
        print('Stop')
    def turn(self, direction):
        print(f"Car turned to {direction}")
    def show_speed(self):
        print(f"Current speed: {self.speed}")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Over speed!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Over speed!')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar(85, "white", "Town")
sport = SportCar(170, "scarlet", "Sport")
work = WorkCar(45, "blue", "Work")
police = PoliceCar(100, "yellow", "Police")

town.show_speed()
work.show_speed()
work.speed = 35
police.turn('Right')