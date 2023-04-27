class Queue:
    def __init__(self, *elements):
        self.data = [elem for elem in elements]

    def __str__(self):  # 1 -> 2 -> 3 -> 4 -> 5
        return ' -> '.join([str(elem) for elem in self.data])

    def append(self, *values):
        for elem in values:
            self.data.append(elem)

    def copy(self):
        return Queue(*self.data.copy())

    def pop(self):
        return self.data.pop(0)


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
# print(q1 == q2, id(q1) == id(q2))
# q3 = q2.next()
# print(q1, q2, q3, sep = '\n')
# print(q1 + q3)
# q3.extend(Queue(1, 2))
# print(q3)
# q4 = Queue(1, 2)
# q4 += q3 >> 4
# print(q4)
# q5 = next(q4)
# print(q4)
# print(q5)
