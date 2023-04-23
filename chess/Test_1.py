from Chess import WHITE, BLACK, Board, Queen, Rook, Bishop, Knight, Pawn
# from Bishop import Bishop
# from Pawn import Pawn

    # Queen, Rook, Bishop, Knight

board = Board()

board.field = [([None] * 8) for i in range(8)]
board.field[0][5] = Rook(0, 5, WHITE)
board.field[1][2] = Bishop(1, 2, WHITE)
board.field[7][6] = Knight(7, 6, BLACK)
w_coords = ((0, 5), (1, 2))
b_coords = ((7, 6), )

print('White:')
for row in range(7, -1, -1):
    for col in range(8):
        if (row, col) in w_coords:
            print('W', end='')
        elif board.is_under_attack(row, col, WHITE):
            print('x', end='')
        else:
            print('-', end='')
    print()
print()

print('Black:')
for row in range(7, -1, -1):
    for col in range(8):
        if (row, col) in b_coords:
            print('B', end='')
        elif board.is_under_attack(row, col, BLACK):
            print('x', end='')
        else:
            print('-', end='')
    print()
