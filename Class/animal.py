class Animal:
    def __init__(self, legs):
        self.legs = legs

    def voice(self):
        print('Animall make some voice.')

    def get_parameters(self):
        return self.legs


class Dog(Animal):
    def __init__(self,legs,type):
        super(Dog, self).__init__(legs)
        self.type = type

    def voice(self):
        print('Gav')

    def print_parameters(self):
        print(super(Dog, self).get_parameters())
