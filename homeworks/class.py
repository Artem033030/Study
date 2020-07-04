import datetime


# class App():
#     def test(self):  # МЕТОД КЛАСА
#         return 'Helo from class'
# instance=App()  # СОЗДАНИЕ ЕКЗЕМПЛЯРА КЛАСА,ИМЯ ЕКЗЕМПЛЯРА КАК ТЕСТ
# print(instance.test()) 
# artem = {'name':'Artem','age':11,'everage':10,}
class Student():
    def __init__(self, name, age, everage, lastname):
        self.lastname = lastname
        self.name = name
        self.age = age
        self.everage = everage

    # дз на 31 - 32
    def full_name(self):
        full_name = self.name + ' ' + self.lastname
        return full_name

    # дз на 31 - 32
    def __str__(self):
        return self.full_name()

    # дз на 31 - 32
    def __repr__(self):
        return f'Student({self.name}, {self.age}, {self.everage}, {self.lastname})'

        # def __repr__(self):
        #
        #     return f'Student({self.name}, {self.age}, {self.everage}, {self.lastname})'

    # дз на 31 - 32
    def __str__(self):
        return f'name is : {self.name},lastname is : {self.lastname},age is : {self.age},everage is : {self.everage}'

    def age1(self, age):
        a = self.age
        now = datetime.datetime.now()
        now_old = now.year - a
        return now_old

    def __gt__(self, other):
        return self.everage > other.everage

    def __lt__(self, other):
        return self.everage < other.everage

    def __eq__(self, other):
        return self.everage == other.everagex

    def __ne__(self, other):
        return self.everage != other.everage

    def __le__(self, other):
        return self.everage <= other.everage

    def __ge__(self, other):
        return self.everage >= other.everage


# Artem = Student('Artem', 15, everage=10, lastname='Pilipchuk')
# print(Artem.name)
# print(Artem.age)
# print(Artem.everage)
# print(Artem.lastname)
# print(Artem.full_name())
# # print('--------------------------------')
Dasha = Student(name='Dasha', age=11, everage=2, lastname='Anohina')
# print(Dasha.name)
# print(Dasha.age)
# print(Dasha.everage)
# print(Dasha.lastname)
Petro = Student(name='Petro', age=10, everage=5, lastname='Kazanin')
# print(Petro.name)
# print(Petro.age)
# print(Petro.everage)
# print(Petro.lastname)
print(Petro < Dasha)
# danya = Student(name='danya', age=11, everage=7, lastname='rybel')
# print(danya.name)
# print(danya.age)
# print(danya.everage)
# print(danya.lastname)
# lesha = Student(name='lesha', age=9, everage=2, lastname='karetko')
# print(lesha.name)
# print(lesha.age)
# print(lesha.everage)
# print(lesha.lastname)
# Alexandra = Student(name='Alexandra', age=10, everage=11, lastname='Bondarenko')
# print(lesha.name)
# print(lesha.age)
# print(lesha.everage)
# print(lesha.lastname)
# vaselina = Student(name='Vaselisa', age=12, everage=9, lastname='Podporina')
# print(vaselina.name)
# print(vaselina.age)
# print(vaselina.everage)
# print(vaselina.lastname)
# Dasho = Student(name='Dasha', age=10, everage=7, lastname='Eshova')
# print(Dasho.name)
# print(Dasho.age)
# print(Dasho.everage)
# print(Dasho.lastname)
# Med_Max = Student(name='Max', age=11, everage=4, lastname='Fomenkov')
# print(Med_Max.name)
# print(Med_Max.age)
# print(Med_Max.everage)
# print(Med_Max.lastname)
# Anya = Student(name='Anya', age=11, everage=4, lastname='Fastship')
# print(Anya.name)
# print(Anya.age)
# print(Anya.everage)
# print(Anya.lastname)
# Elizaveta = Student(name='Liza', age=10, everage=9, lastname='Mruxnich')
# print(Elizaveta.name)
# print(Elizaveta.age)
# print(Elizaveta.everage)
# print(Elizaveta.lastname)
# Eva = Student(name='Eva', age=10, everage=5, lastname='papariga')
# print(Eva.name)
# print(Eva.age)
# print(Eva.everage)
# print(Eva.lastname)
# Masha = Student(name='Masha', age=11, everage=6, lastname='Pavlova')
# print(Masha.name)
# print(Masha.age)
# print(Masha.everage)
# print(Masha.lastname)
# kris = Student(name='Kristian', age=10, everage=7, lastname='Ayzinsh')
# print(kris.name)
# print(kris.age)
# print(kris.everage)
# print(kris.lastname)
# Andrev = Student(name='Andrev', age=10, everage=9, lastname='Tkachenko')
# print(Andrev.name)
# print(Andrev.age)
# print(Andrev.everage)
# print(Andrev.lastname)
# roma = Student(name='roma', age=11, everage=0, lastname='bereznak')
# print(roma.name)
# print(roma.age)
# print(roma.everage)
# print(roma.lastname)
# Nasta_o = Student(name='Nasta', age=9, everage=3, lastname='Ogrisco')
# print(Nasta_o.name)
# print(Nasta_o.age)
# print(Nasta_o.everage)
# print(Nasta_o.lastname)
# Alex = Student(name='Alex', age=10, everage=8, lastname='Geza')
# print(Alex.name)
# print(Alex.age)
# print(Alex.everage)
# print(Alex.lastname)
# Nasta = Student(name='Nasta', age=9, everage=2, lastname='Novitska')
# print(Nasta.name)
# print(Nasta.age)
# print(Nasta.everage)
# print(Nasta.lastname)
# olga = Student(name='olga', age=41, everage=0, lastname='zebid')
# print(olga.name)
# print(olga.age)
# print(olga.everage)
# print(olga.lastname)
# anna = Student(name='anna', age=21, everage=0, lastname='tepidco')
# print(anna.name)
# print(anna.age)
# print(anna.everage)
# print(anna.lastname)
# for x in range(0, 13):
#     print(x)

# ОБРАЩАЕМСЯ К МЕТОДУ КЛАСА ТАК:ИМЯ ЕКЗЕМПЛЯРА ТОЧКА ИМЯ МЕДОТА КРУГЛЫЕ СКАБКИ С АРГУМЕНТАМИ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
