data = []
dic = {}
while True:
    st = input().split()
    if not st:
        break
    if st[2][2] == ']':
        num = int(st[2][1])
    else:
        num = int(st[2][1] + st[2][2])
    if num > 5:
        dic[st[1]] = num
for elem in dic:
    print(f' - {elem} [{dic[elem]}]')
print()
