class Calculator:

    def __init__(self):
        self.a = 0, 000
        self.b = 0, 000
        self.result = 0, 000


    def _add(self):
        return self.a + self.b

    def _substr(self):
        return self.a - self.b

    def _mult(self):
        return self.a * self.b

    def _div(self):
        return self.a / self.b

    def act(self, action, a, b):
        self.a = a
        self.b = b
        if action == '+':
            self.result = self._add()
            print(self.a)
            print("+")
            print(self.b)
            print('-------------')


        if action == '-':
            self.result = self._substr()
            print(self.a)
            print("-")
            print(self.b)
            print('-------------')

        if action == '*':
            self.result = self._mult()
            print(self.a)
            print("*")
            print(self.b)
            print('-------------')

        if action == '/':
            self.result = self._div()
            print(self.a)
            print("/")
            print(self.b)
            print('-------------')
        return self.result


calc = Calculator()
add = calc.act("*", 1.006, 2.005)
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
