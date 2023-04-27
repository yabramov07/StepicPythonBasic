class SeaMap:
    def __init__(self):
        # self.data = ['.' * 10].copy() * 10
        self.data = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

    def shoot(self, row0, col0, result):
        row = row0 - 1
        col = col0 - 1
        if result == 'miss':
            self.data[row][col] = '*'
        elif result == 'hit':
            self.data[row][col] = 'x'
        elif result == 'sink':
            self.data[row][col] = 'x'
            lis = [[row, col]]
            used = []
            while True:
                if len(lis) == 0:
                    break
                row_ = lis[0][0]
                col_ = lis[0][1]
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if self.data[row_ + j][col_ + i] == '.':
                            self.data[row_ + j][col_ + i] = '*'
                        elif self.data[row_ + j][col_ + i] == 'x' and self.data[row_ + j][col_ + i] == \
                                self.data[row_][col_] and self.data[row_ + j][col_ + i] not in used:
                            lis.append([row_ + j, col_ + i])
                        if i == 1 and j == 1:
                            used.append(lis[0])
                            lis.pop(0)

    def cell(self, row, col):
        return self.data[row - 1][col - 1]


sm = SeaMap()
sm.shoot(2, 0, 'miss')
sm.shoot(6, 9, 'miss')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()



