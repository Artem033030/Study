from fractions import Fraction


class Calculator:

    def __init__(self):
        # # self.a = round(1,000)
        # # self.b = round(1,000)
        # self.a = float(round(a(1,000)))
        # self.b = float(round(b(1,000)))
        # self.a = float(round(0,000))
        # self.b = float(round(0,000))
        # self.result = (0,000)
        self.a = 0,000
        self.b = 0,000
        self.result = 0, 000
        self.chain = [self.a]
        # self.chain.append(self.b)

    def _add(self):
        self.chain.append('+')
        self.chain.append(self.b)
        self.chain.append('=')

        return self.a + self.b

    def _substr(self):
        self.chain.append("-")
        self.chain.append(self.b)
        self.chain.append('=')
        return self.a - self.b

    def _mult(self):
        self.chain.append('*')
        self.chain.append(self.b)
        self.chain.append('=')
        return self.a * self.b

    def _div(self):
        self.chain.append('/')
        self.chain.append(self.b)
        self.chain.append('=')
        return self.a / self.b

    def act(self, action, a, b, ):
        # self.a = float(a)
        # self.b = float(b)
        # self.a = float(round(a(0,000)))
        # self.b = float(round(b(0,000)))
        # self.a = round(float(1, 000))
        # self.b = round(float(1, 000))
        # self.a = float(round(0,000))
        # self.b = float(round(0,000))
        self.a = float(a)
        self.b = float(b)  # ПРОЧЕТАТЬ ПРО ЗНАЧЕНИЯ АРГУМЕНТОВ ПО УМОЛЧЯНИЮ

        if action == '+':
            self.result = self._add()

        if action == '-':
            self.result = self._substr()

        if action == '*':
            self.result = self._mult()

        if action == '/':
            self.result = self._div()
        # chain = [self.a, action, self.b, '=', self.result]

        # if self.b is None:
        #     self.b = chain[4]
        # n = chain[4]
        # chain.append(self.a)
        # if self.result == n:
        #     .append(action)
        #     d.append(self.b)
        #     d.append('=')
        #     d.append(self.result)
        #     print(d)
        self.chain.append(self.result)
        return self.result


calc = Calculator()
add = calc.act("*", 1, 2)
print(add)


# print(1)
# if add == 3:
#     print("done")
# else:
#     print('nope')
# sub = calc.act("-", 1, 2)
# print(2)
# if sub == -1:
#     print("done")
# else:
#     print('nope')
# mult = calc.act("*", 1, 2)
# print(3)
# if mult == 2:
#     print("done")
# else:
#     print('nope')
# div = calc.act("/", 1, 2)
# print(4)
# if div == 0.5:
#     print("done")
# else:
#     print('nope')
# class thousandth(Calculator):

class One(Calculator):
    def __init__(self):
        self.b = super(Calculator, self).__init__(self.b, self.a, self.result)

    def colk(self):
        counter = []
        for x in self.result:
            counter.append(x)
        if self.b == 0:
            self.b = counter[::-1]


class Two(Calculator):
    def __init__(self):
        self.x = super(Calculator, self).__init__(self.b, self.a, self.result)

    def upp(self):
        chein = []
        for check in self.a:
            chein.append(check)

















