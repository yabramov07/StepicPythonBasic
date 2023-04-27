class Polynomial:
    def __init__(self, coefficients):
        # self.data = [elem for elem in coefficients]
        self.data = coefficients

    def __call__(self, x):
        sum = 0
        for i in range(len(self.data)):
            sum += self.data[i] * x ** i
        return sum

    def __add__(self, other):
        lis = []
        for i in range(max([len(self.data), len(other.data)])):
            w = max([len(self.data), len(other.data)])
            len_self = len(self.data)
            len_other = len(other.data)
            if len(self.data) - 1 >= i and len(other.data) - 1 >= i:
                lis.append(self.data[i] + other.data[i])
            elif len(self.data) - 1 >= i > len(other.data) - 1:
                lis.append(self.data[i])
            elif len(other.data) - 1 >= i > len(self.data) - 1:
                lis.append(other.data[i])
        return Polynomial(lis)


poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))
