#Практическое задание №8_Задача №1

class Date:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def extract(cls, dd_mm_yyyy):
        my_date = []
        for i in dd_mm_yyyy.split():
            if i != '-':
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(dd, mm, yyyy):
        import datetime
        correctDate = None
        try:
            newDate = datetime.datetime(yyyy, mm, dd)
            correctDate = True
            print('Формат даты верный')
        except ValueError:
            correctDate = False
            print('Формат даты неверный')
    def __str__(self):
        return f'Текущая дата {Date.extract(self.dd_mm_yyyy)}'

today = Date('28 - 11 - 2021')
print(today)
print(Date.valid(28, 10, 2022))
print(Date.valid(29, 2, 2024))#2024 год - високосный, у него в феврале 29 дней
print(Date.valid(29, 2, 2022))