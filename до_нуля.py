try:
    isShow = True
    while True:
        i = input()
        i = int(i)
        if i == 0:
            isShow = False
        if isShow:
            print(i)
except EOFError:
    pass

