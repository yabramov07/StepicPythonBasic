n = int(input())
while n > 0:
    if n > 3:
        i = 1
    else:
        i = n
    n -= i
    print(i, n)
    if n == 0:
        print("ИИ выиграл!")
        break
    a = int(input())
    if 0 < a <= 3 and n - a >= 0:
        n -= a
        print(a, n)
        if n == 0:
            print("Вы выиграли!")
            break