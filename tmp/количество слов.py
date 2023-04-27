dic = {}
num = int(input('Номер слова в строке: ')) - 1
st_ = input('Слово, которое вставляем на место X: ')
while True:
    st = input().lower().split()
    if not st:
        break
    if st[num] not in dic:
        dic[st[num]] = 1
    else:
        dic[st[num]] += 1
print()
print(f'Все варианты w, если X = {st_}, на сайте НКРЯ:')
for elem in dic:
    if dic[elem] > 0:
        print(f' - {elem} [{dic[elem]}]')
print('-_-_-_' * 5)
