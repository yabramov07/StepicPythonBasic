# a * x ** 2 + b * x + c = 0
# import math
# print(dir(math))
from math import sqrt


def discriminant(a, b, c):
    d = sqrt(b ** 2 - 4 * a * c)
    return (-1 * b - d) / (2 * a), (-1 * b + d) / (2 * a)


def arithmetic_progression_n(a1, d, n):
    return a1 + (n - 1) * d


def arithmetic_progression_summ1(a1, an, n):
    return (a1 + an) * n / 2


def arithmetic_progression_summ2(a1, d, n):
    return 2 * a1 + d * (n - 1) / 2 * n


def geometric_progression_n(b1, q, n):
    return b1 * q ** (n - 1)


def geometric_progression_summ1(b1, q, n):
    return b1 * (1 - q ** n) / (1 - q)


def geometric_progression_summ2(d1, dn, q):
    return (dn * q - d1) / (q - 1)


def simple_interest(s0, k):
    return s0 * (1 + k / 100)


# lis = []
# check = []
# number = 0
# while True:
#     st = input()
#     if not st:
#         break
#     if st in '123456':
#         number += 1
#         check.append(number)
#     if st in '12345':
#         lis.append(0)
#     elif int(st) == 6:
#         lis.append(1)
# for i in range(len(check)):
#     if i == 0:
#         print('|', '\t', check[i], '\t', '|', sep='', end='\t')
#     elif i == len(check) - 1:
#         print(check[i], '\t', '|', sep='')
#     else:
#         print(check[i], '\t', '|', sep='', end='\t')
# print('--------' * len(lis))
# for i in range(len(lis)):
#     if i == 0:
#         print('|', '\t', lis[i], '\t', '|', sep='', end='\t')
#     else:
#         print(lis[i], '\t', '|', sep='', end='\t')


# device = input('"Монета" or "Кость": ')
# if device == 'Монета':
#     print(0.5 ** int(input('T = ')))
# elif device == 'Кость':
#     m = int(input('Сколько граней у кости: '))
#     n = len(input('Какие числа являются p: ').split())
#     print(((6 - n) / m) ** (int(input('T = ')) - 1) * (n / m))

data = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
s = 0
for i in range(3):
    for j in range(3):
        if data[i][j] == '-':
            s += 1
if s == 0:
    print('YES')
else:
    print(s)

