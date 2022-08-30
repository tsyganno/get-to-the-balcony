class Matrix:

    def __init__(self):
        self.counter = 0
        self.step_dict = {
            0: 'Север',
            1: 'Восток',
            2: 'Юг',
            3: 'Запад'
        }
        self.matrix = [
            [0, 'Балкон', 0],
            ['Спальня', 'Холл', 'Кухня'],
            ['Подземелье', 'Коридор', 'Оружейная']
        ]
        self.location = 'Подземелье'

    def movement(self, path: int, step: int):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == self.location:
                    index_i = i
                    index_j = j








