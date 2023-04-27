from Queen2 import (
    Board, Pawn, Rook, King, Knight, Bishop, Queen,
    WHITE, BLACK
)

board = Board()
board.field = [([None] * 8) for i in range(8)]
queen = Queen(BLACK)
r0, c0 = 4, 5
board.field[r0][c0] = queen
board.field[4][2] = Pawn(BLACK)
board.field[6][5] = Pawn(WHITE)

for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, r0, c0, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()