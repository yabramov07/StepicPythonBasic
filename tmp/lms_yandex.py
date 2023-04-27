# def x(st):
#     return st[0].upper() + st[1:]
#
#
# from random import choice, randrange, randint
# name = input().split()
# number = int(input())
# diap = input().split()
# full_value = float(input())
# lis_n = []
# lis_num = []
# calor = []
# for i in range(number):
#     st = choice(name)
#     lis_n.append(st)
#     name.remove(st)
#     lis_num.append(randint(int(diap[0]), int(diap[1])))
#     calor.append((randrange(0, int(full_value * 100))) / 100)
# for i in range(number):
#     print(x(lis_n[i]), lis_num[i], 'of pieces, calorie content', calor[i], 'kkal, total caloric', calor[i] * lis_num[i])


# <Name> <number> of pieces, calorie content <calorie value> kkal, total caloric <full_value>


import datetime as dt


def x(y):
    y -= 1
    if y == -1:
        y = 6
    return y


data = '01-03-2021'
d = dt.datetime.strptime(data, '%d-%m-%Y')
print(d)
for i in range(1, 10):
    data_time = d + dt.timedelta(days=i)
    print(data_time, x(int(data_time.strftime('%w'))))
    data_time.strftime('%w')



import datetime

# today = datetime.datetime.now()
# today.strftime('%Y-%m-%d')
# print(today)
# 0 3 5
# 3
