import pymorphy2
morph = pymorphy2.MorphAnalyzer()

dic = {}
list1 = []
list2 = []
form = input('normal_form / not normal_form')
if form == 'normal_form':
    list1_n = []
    list2_n = []
    while True:
        st = input().lower().split()
        if not st:
            break
        list1.append(st[1])
    for i in range(len(list1)):
        x = morph.parse(list1[i])[0]
        st = x.normal_form
        list1_n.append(st)
    print('-_-_-_' * 5)
    while True:
        st = input().lower().split()
        if not st:
            break
        list2.append(st[1])
    for i in range(len(list2)):
        x = morph.parse(list2[i])[0]
        st = x.normal_form
        list2_n.append(st)
    for i in range(len(list1_n)):
        if list1_n[i] in list2_n and list1_n[i] not in dic:
            dic[list1_n[i]] = 1
        elif list1_n[i] in list2_n and list1_n[i] in dic:
            dic[list1_n[i]] += 1
    for elem in dic:
        print(f'{elem} [{dic[elem]}]')
elif form == 'not normal_form':
    dic = {}
    list1 = []
    list2 = []
    while True:
        st = input().lower().split()
        if not st:
            break
        list1.append(st[1])
    print('-_-_-_' * 5)
    while True:
        st = input().lower().split()
        if not st:
            break
        list2.append(st[1])
    for i in range(len(list1)):
        if list1[i] in list2 and list1[i] not in dic:
            dic[list1[i]] = 1
        elif list1[i] in list2 and list1[i] in dic:
            dic[list1[i]] += 1
    for elem in dic:
        print(f'{elem} [{dic[elem]}]')
    print()
