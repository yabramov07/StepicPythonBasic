def ray_1(x, y, row, col):
    data = []
    while y != 7:
        y += 1
        data.append([x, y])
        if y == 7 and [row, col] in data:
            return data


def ray_2(x, y, row, col):
    data = []
    while x != 7 and y != 7:
        x += 1
        y += 1
        data.append([x, y])
        if y == 7 and x == 7 and [row, col] in data:
            return data


def ray_3(x, y, row, col):
    data = []
    while x != 7:
        x += 1
        data.append([x, y])
        if x == 7 and [row, col] in data:
            return data


def ray_4(x, y, row, col):
    data = []
    while x == 7 and y == 0:
        x += 1
        y -= 1
        data.append([x, y])
        if x == 7 and y == 0 and [row, col] in data:
            return data


def ray_5(x, y, row, col):
    data = []
    while y == 0:
        y -= 1
        data.append([x, y])
        if y == 0 and [row, col] in data:
            return data


def ray_6(x, y, row, col):
    data = []
    while x == 0 and y == 0:
        x -= 1
        y -= 1
        data.append([x, y])
        if x == 0 and y == 0 and [row, col] in data:
            return data


def ray_7(x, y, row, col):
    data = []
    while x == 0:
        x -= 1
        data.append([x, y])
        if x == 0 and [row, col] in data:
            return data


def ray_8(x, y, row, col):
    data = []
    while x == 0 and y == 7:
        x -= 1
        y += 1
        data.append([x, y])
        if x == 0 and y == 7 and [row, col] in data:
            return data
