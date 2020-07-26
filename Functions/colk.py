class Calculator:

    def __init__(self):
        self.a = None
        self.b = None
        self.result = None

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
            return self.result

        if action == '-':
            self.result = self._substr()
            return self.result

        if action == '*':
            self.result = self._mult()
            return self.result

        if action == '/':
            self.result = self._div()
            return self.result


calc = Calculator()
calc.act(2)
calc.act(3)
print(calc.act('+'))
calc.act(2)
calc.act(3)
print(calc.act('-'))
calc.act(2)
calc.act(3)
print(calc.act('*'))
calc.act(2)
calc.act(3)
print(calc.act('/'))
