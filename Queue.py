class Queue:
    def __init__(self, *elements):
        self.data = [elem for elem in elements]

    # склейка очередей создаёт новую увеличенную очередь
    def __add__(self, other):
        return self.data + other.data

    # расширяет первую очередь второй
    def __iadd__(self, other):
        self.data = self.data + other.data
        return self.data

    # проверяет очереди на равенство всех элементов. Возвращает True или False.
    def __eq__(self, other):
        return self.data == other.data

    # создаёт новую очередь без первых N (вышедших) элементов.
    # В случае, когда N превышает количество элементов очереди, следует вернуть пустую очередь.
    def __rlshift__(self, other):  # other << self
        if other > len(self.data):
            return []
        lis = []
        for i in range(other, len(self.data)):
            lis.append(self.data[i])
        return lis

    # добавляет несколько значений в конец очереди (как минимум одно)
    def append(self, *values):
        for e in values:
            self.data.append(e)

    #  создаёт копию данной очереди, то есть возвращает новую очередь,
    #  полностью аналогичную исходной
    def copy(self):
        return [self.data]

    # вытаскивает и возвращает первый элемент очереди,
    # при этом этот элемент из очереди удаляется.
    # Если очередь пуста, то возвращает None.
    def pop(self):
        elem_1 = self.data[0]
        self.data.pop(0)
        return elem_1

    #  расширяет данную очередь другой,
    #  то есть приклеивает вторую очередь к первой
    def extend(self, queue):
        for e in queue:
            self.data.append(e)

    #  возвращает новую очередь, начинающуюся со второго элемента текущей
    def next(self):
        lis = []
        for i in range(1, len(self.data)):
            lis.append(self.data[i])
        return lis

    # [1 -> 2 -> 3 -> 4 -> 5],
    def __str__(self):
        return "[" + " -> ".join([str(x) for x in self.data]) + "]"


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)

q2 = Queue(1, 2, 3)

q3 = q1 + q2