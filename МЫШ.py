import pymorphy2
morph = pymorphy2.MorphAnalyzer()

st = 'будет'
# st = input()
data = []
end = []
while True:
    st = input().lower()
    if st == 'str':
        break
    st = st.split()
    for elem in st:
        data.append(elem)
data_len = len(data)
# print(data)
for i in range(len(data)):
    used = []
    data_i = data[i]
    if data[i] == 'будет' and data[i - 1] == 'снег':
        used.append(data[i - 1])
        used.append(data[i])
        used.append(data[i + 1])
        end.append(used)
print('-_-_-_' * 10)
# for elem in data:
#     x = morph.parse(elem)[0]
#     st = x.normal_form
for elem in end:
    print(' '.join(elem))
print('-_-_-_' * 5)
