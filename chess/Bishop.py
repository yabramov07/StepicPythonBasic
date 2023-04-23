# Слон
class Bishop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if row < 0 or row > 7 or col < 0 or col > 7:
            return False
        dx = abs(self.row - row)
        dy = abs(self.col - col)
        return dx == dy

