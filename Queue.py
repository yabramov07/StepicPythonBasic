class Queue:
    def __init__(self, *elements):
        self.data = [e for e in elements]

    # добавляет несколько значений в конец очереди (как минимум одно)
    def append(self, *values):
        for e in values:
            self.data.append(e)

    def copy(self):
        return [self.lis]

    # вытаскивает и возвращает первый элемент очереди,
    # при этом этот элемент из очереди удаляется.
    # Если очередь пуста, то возвращает None.
    def pop(self):
        elem_1 = self.data[0]
        self.data.pop(0)
        return elem_1

    def extend(self, queue):
        pass

    def next(self):
        pass

    # [1 -> 2 -> 3 -> 4 -> 5],
    def __str__(self):
        return "[" + " -> ".join([str(x) for x in self.data]) + "]"

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)

q2 = Queue(1, 2, 3)

q3 = q1 + q2