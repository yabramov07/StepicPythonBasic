WHITE = 1
BLACK = 2


# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    # Создаём шахматную доску
    board = Board()
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход черных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Rook:  # Ладья

    def __init__(self, color):
        self.color = color

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, rowTo, colTo):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row != rowTo and col != colTo:
            return False

        return True


class King:
    def __init__(self, color):
        self.color = color

    def char(self):
        return 'K'

    def get_color(self):
        return self.color

    # Возвращает None, если путь невозможен и список клеток, если возможен
    def can_move(self, board, row, col, rowTo, colTo):
        if rowTo < 0 or rowTo > 7 or colTo < 0 or colTo > 7:
            return None
        if (row + 1 == rowTo or row - 1 == rowTo or row == rowTo) and \
                (col + 1 == colTo or col - 1 == colTo or col == colTo):
            return [rowTo, colTo]


class Bishop:  # Слон
    def __init__(self, color):
        self.color = color

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, rowTo, colTo):
        if row < 0 or row > 7 or col < 0 or col > 7:
            return False
        dx = abs(row - rowTo)
        dy = abs(col - colTo)
        return dx == dy


class Pawn:  # Пешка
    def __init__(self, color):
        self.color = color

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, rowTo, colTo):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != colTo:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == rowTo:
            return True

        # ход на 2 клетки из начального положения
        if row == start_row and row + 2 * direction == rowTo:
            return True

        return False


class Knight:  # Конь
    def __init__(self, color):
        self.color = color

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, rowTo, colTo):
        if row < 0 or row > 7 or col < 0 or col > 7:
            return False
        dx = abs(row - rowTo)
        dy = abs(col - colTo)
        return dx + dy == 3 and (dx == 1 or dy == 1)


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)

        self.field[0][0] = Rook(WHITE)
        self.field[0][1] = Knight(WHITE)
        self.field[0][2] = Bishop(WHITE)
        self.field[0][3] = Queen(WHITE)
        self.field[0][4] = King(WHITE)
        self.field[0][5] = Bishop(WHITE)
        self.field[0][6] = Knight(WHITE)
        self.field[0][7] = Rook(WHITE)
        self.field[1][0] = Pawn(WHITE)
        self.field[1][1] = Pawn(WHITE)
        self.field[1][2] = Pawn(WHITE)
        self.field[1][3] = Pawn(WHITE)
        self.field[1][4] = Pawn(WHITE)
        self.field[1][5] = Pawn(WHITE)
        self.field[1][6] = Pawn(WHITE)
        self.field[1][7] = Pawn(WHITE)
        self.field[7][0] = Rook(BLACK)
        self.field[7][1] = Knight(BLACK)
        self.field[7][2] = Bishop(BLACK)
        self.field[7][3] = Queen(BLACK)
        self.field[7][4] = King(BLACK)
        self.field[7][5] = Bishop(BLACK)
        self.field[7][6] = Knight(BLACK)
        self.field[7][7] = Rook(BLACK)
        self.field[6][0] = Pawn(BLACK)
        self.field[6][1] = Pawn(BLACK)
        self.field[6][2] = Pawn(BLACK)
        self.field[6][3] = Pawn(BLACK)
        self.field[6][4] = Pawn(BLACK)
        self.field[6][5] = Pawn(BLACK)
        self.field[6][6] = Pawn(BLACK)
        self.field[6][7] = Pawn(BLACK)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(self, row, col, row1, col1):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                f = self.field[i][j]
                if f is not None and f.get_color() == color and f.can_move(row, col):
                    return True

        return False

    def get_piece(self, row, col):
        return self.field[row][col]

    def __str__(self):
        lines = ['     +----+----+----+----+----+----+----+----+']
        for row in range(7, -1, -1):
            line = '  ' + str(row) + '  '
            for col in range(8):
                line += '| ' + self.cell(row, col) + ' '
            lines.append(line + '|')
            lines.append('     +----+----+----+----+----+----+----+----+')
        lines.append('        ' + '    '.join([str(col) for col in range(8)]))

        return '\n'.join(lines)


class Queen:  # Ферзь
    def __init__(self, color):
        self.color = color

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, rowTo, colTo):
        # return None
        if row < 0 or row > 7 or col < 0 or col > 7:
            return False
        dx = abs(row - rowTo)
        dy = abs(col - colTo)

        if dx == dy or (dx == 0 and dy > 0) or (dx > 0 and dy == 0):
            path = find_path(row, col, sign(rowTo - row), sign(colTo - col), rowTo, colTo)

            # проверяем свободен ли путь
            if path:
                for i in range(1, len(path)):
                    piece = board.get_piece(*path[i])
                    if piece and i < len(path) - 1:
                        return False

                    # если это последняя клетка
                    if i == len(path) - 1:
                        if piece:
                            # проверяем что фигуру на последней клетке можно съесть
                            return piece.get_color() != self.color
                        else:
                            return True

        return False


def find_path(start_row, start_col, dx, dy, row_to, col_to):
    path = []
    for i in range(0, 8):
        x = start_row + dx * i
        y = start_col + dy * i
        if x < 0 or x > 7 or y < 0 or y > 7:
            return None
        path.append([x, y])
        if x == row_to and y == col_to:
            return path

    return None


def sign(num):
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1