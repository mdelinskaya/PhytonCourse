#Практическое занятие №7_Задача №1.
class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0, 0],
                [0, 0, 0, 0]]
        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

matrix = Matrix([[2, 3, 11, 15],
                [1, 5, 14, 20]],
                [[3, 7, 9, 15],
                 [4, 5, 6, 10]])

print(matrix.__add__())