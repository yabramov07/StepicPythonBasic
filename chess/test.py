from Chess import *

board = Board()
board.move_piece(1, 1, 3, 1) #Белая пешка на две клетки вперед
board.move_piece(6, 1, 4, 1) #Черная пешка на две клетки на встречу
print(board)
board.move_piece(0, 2, 2, 0) #Белый слон (Bishop) влево
if board.move_piece(4, 1, 3, 1): #Черная пешка на место белой, типо съела
    print(board)
else:
    print('Error')