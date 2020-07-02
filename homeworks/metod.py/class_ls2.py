class Animal():
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def voice(self):
        return 'make some noise'

    def eat(self):
        return f"{self.name} eating"


Barcik = Animal(name='Barcik', age=100)
print(Barcik.eat())


class Dog(Animal):
    def __init__(self, name, age, type):
        super(Dog, self).__init__(age, name)
        self.type = type

    def voice(self):
        return 55


bobik_Chihua = Dog('Bobik', 15, "Chihua_hua")
print(bobik_Chihua.name)
print(bobik_Chihua.eat())
print(bobik_Chihua.voice())


class Humen():
    def __init__(self, eat, drink, type):
        self.eat = eat
        self.drink = drink
        self.type = type

    def work(self):
        return 'He,She work'

    def eat(self):
        return f"{self.name} eating"


class Man(Humen):
    def __init__(self, eat, drink, type, work):
        super(Man, self).__init__(eat, drink, type)
        self.work = work

    def work(self):
        return 'He is work'


class Women(Humen)
    def __init__(self, eat, drink, type, cook):
        super(Woman, self).__init__(eat, drink, type, cook)
        self.cook = cook
