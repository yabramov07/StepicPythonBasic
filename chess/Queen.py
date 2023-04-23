# Ферзь
class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if row < 0 or row > 7 or col < 0 or col > 7:
            return False
        dx = abs(self.row - row)
        dy = abs(self.col - col)
        return dx == dy or (dx == 0 and dy > 0) or (dx > 0 and dy == 0)


WHITE=1
BLACK=2

row0 = 7
col0 = 3
queen = Queen(row0, col0, BLACK)

print('white' if queen.get_color() == WHITE else 'black')
for row in range(8, -2, -1):
    for col in range(-1, 9):
        if row == row0 and col == col0:
            print(queen.char(), end='')
        elif queen.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()