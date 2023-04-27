from Queen2 import (
    Board, Pawn, Rook, King, Knight, Bishop, Queen,
    WHITE, BLACK
)

board = Board()
board.field = [([None] * 8) for i in range(8)]
queen = Queen(WHITE)
r0, c0 = 0, 1
board.field[r0][c0] = queen
board.field[2][4] = Knight(BLACK)
board.field[4][4] = Knight(WHITE)
board.field[6][3] = Knight(WHITE)

for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, r0, c0, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()
print()

r1, c1 = 2, 3
board.move_piece(r0, c0, r1, c1)

print('after move')
for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, r1, c1, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()
print()