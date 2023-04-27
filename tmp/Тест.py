import pymorphy2
morph = pymorphy2.MorphAnalyzer()




# import morph as morph
# import pymorphy2
#
# # inflect
# morph = pymorphy2.MorphAnalyzer()
# import sys
#
# number = 0
# lis0 = ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть']
# data = list(map(str.strip, sys.stdin))
# data1 = "".join(data).split('.')
# data2 = ''.join(data1).split(',')
# lis = ''.join(data2).lower().split()
# print(lis)
# for i in range(len(lis)):
#     res = morph.parse(lis[i])[1]
#     if "VERB" in res.tag:
#
#     if lis[i] in lis0:
#         number += 1
# print(number)
