class TicTacToeBoard:
    def __init__(self):
        self.data = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.num = 0  # номер хода
        self.end = 'str'  # победитель
        self.flag = False  # завершена ли игра

    def new_game(self):  # сброс
        self.data = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.num = 0
        self.end = 'str'
        self.flag = False

    def get_field(self):
        return self.data

    def check_field(self):  # проверка на победителя
        if self.flag:
            if self.end == 'X':
                return 'X'
            elif self.end == '0':
                return '0'
            else:
                return 'D'
        else:
            return 'None'

    def make_move(self, row, col):
        if self.data[row - 1][col - 1] == '-' and not self.flag:
            if self.num % 2 == 0:
                self.data[row - 1][col - 1] = 'X'
                self.num += 1
            else:
                self.data[row - 1][col - 1] = '0'
                self.num += 1
        elif self.data[row - 1][col - 1] != '-' and not self.flag:
            return f'Клетка {row}, {col} уже занята'
        elif self.flag:
            return 'Игра уже завершена'
        if (self.data[0][0] == self.data[0][1] == self.data[0][2] or self.data[0][0] == self.data[1][0] ==
            self.data[2][0] or self.data[0][0] == self.data[1][1] == self.data[2][2]) and self.data[0][0] == 'X' \
                or (self.data[1][0] == self.data[1][1] == self.data[1][2] or self.data[2][0] == self.data[1][1] ==
                    self.data[0][2] or self.data[0][1] == self.data[1][1] == self.data[2][1]) and self.data[1][1] == \
                'X' \
                or (self.data[2][0] == self.data[2][1] == self.data[2][2] or self.data[0][2] == self.data[0][1] ==
                    self.data[0][2]) and self.data[2][2] == 'X':
            self.flag = True
            self.end = 'X'
        elif (self.data[0][0] == self.data[0][1] == self.data[0][2] or self.data[0][0] == self.data[1][0] ==
              self.data[2][0] or self.data[0][0] == self.data[1][1] == self.data[2][2]) and self.data[0][0] == '0' \
                or (self.data[1][0] == self.data[1][1] == self.data[1][2] or self.data[2][0] == self.data[1][1] ==
                    self.data[0][2] or self.data[0][1] == self.data[1][1] == self.data[2][1]) and self.data[1][1] == \
                '0' \
                or (self.data[2][0] == self.data[2][1] == self.data[2][2] or self.data[0][2] == self.data[0][1] ==
                    self.data[0][2]) and self.data[2][2] == '0':
            self.flag = True
            self.end = '0'
            s = 0
            for i in range(3):
                for j in range(3):
                    if self.data[i][j] == '-':
                        s += 1
            if s == 0 and self.end == 'str':
                self.end = 'D'
        if self.flag and self.end != 'D':
            return f'Победил игрок {self.end}'
        elif self.end == 'D':
            return 'Ничья'
        else:
            return 'Продолжаем играть'
