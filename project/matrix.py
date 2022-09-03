class Matrix:

    def __init__(self):
        self.counter = 0
        self.matrix = [
            [0, 'Балкон', 0],
            ['Спальня', 'Холл', 'Кухня'],
            ['Подземелье', 'Коридор', 'Оружейная']
        ]
        self.location = 'Подземелье'

    def movement(self, path: int, step: int):
        index_i = ''
        index_j = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == self.location:
                    index_i = i
                    index_j = j
        if path == 1:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i == index_i and j == index_j + step:
                        if self.matrix[i][j] is not (None, 0):
                            self.location = self.matrix[i][j]
                            return self.location
        elif path == 3:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i == index_i and j == index_j - step:
                        if self.matrix[i][j] is not (None, 0):
                            self.location = self.matrix[i][j]
                            return self.location
        elif path == 0:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i == index_i - step and j == index_j:
                        if self.matrix[i][j] is not (None, 0):
                            self.location = self.matrix[i][j]
                            return self.location
        elif path == 2:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i == index_i + step and j == index_j:
                        if self.matrix[i][j] is not (None, 0):
                            self.location = self.matrix[i][j]
                            return self.location













