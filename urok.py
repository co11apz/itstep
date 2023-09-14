# from functools import reduce
# def fn_reduce(a, b):
#     return a * b
#
# class Calculator:
#     MODEL = 'CITIZEN'
#
#     def __init__(self, seria):
#         self._seria = seria
#         self._result = None
#         self.mem = None
#
#     def memory(self):
#         self.mem = self._result
#
#     def get_memory(self):
#         return self.mem
#
#     def clear_mem(self):
#         self.mem = None
#
#     def clear(self):
#         self._result = None
#
#     @property
#     def result(self):
#         print(self._result)
#         return self._result
#
#     @result.setter
#     def result(self, value):
#         if isinstance(value, int) or isinstance(value, float):
#             self._result = value
#         else:
#             raise TypeError('Result is always number')
#
#     def sum(self, *args):
#         try:
#             self._result = sum(args)
#             self._result
#         except TypeError as exc:
#             print('Only numbers allowed \n', exc)
#         return self
#
#     def multiply(self, *args):
#         try:
#             res = reduce(lambda x, y: x * y, args)
#             self.result = res
#         except TypeError:
#             self.clear()
#             print('only numbers mult')
#         self.result
#         return self
#
# c = Calculator(seria = '3453456346')
#
# c.sum(1, 2, 3).memory()
# # c.result
# # c.result = 'dom'
# # c.result
# c.multiply(2, 2, 3).sum(c.get_memory(), c.result)
import datetime


class Child:
    COUNTRY = 'Belarus'

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = 0
        self.birthday = datetime.datetime.now()
        print(self.name)

    @classmethod
    def new_born(cls):
        print('new_born age is 0')

    @staticmethod
    def some_count():
        print('count ship...')

    def cry(self):
        print(f'{self.name} aaaaaaaaaaaaaaaaa')

c = Child('Johnny', 'Wick', 'M')
# c.new_born()
# print(c.__class__, 'class of c')
# Child.new_born()
# c.some_count()
# Child.some_count()
class YoungMan(Child):

    def __init__(self, name, surname, gender, birthday):
        super().__init__(name, surname, gender)
        self.birthday = birthday
        current_year = datetime.date.today().year
        self.age = current_year - self.birthday.year

    def go_to_school(self):
        print(f'{self.name} going to school')

dob = datetime.date(2000, 7, 25)

y = YoungMan('Mason', 'Merlin', 'M', dob)
# y.cry()
# c.cry()
# y.go_to_school()
# print(c.birthday, 'child')
# print(y.age, 'y_man')
class Actors:
    def improvization(self):
        print('do some stuff...')
class Adult(YoungMan):
    def __init__(self, name, surname, gender, birthday, profession):
        super().__init__(self, name, surname, gender, birthday)
        self.profession = profession

    def go_to_school(self):
        raise NotImplemented('too old =(')
dob1 = datetime.date(1995, 8, 10)
adult = Adult('Emma', 'Stone', 'FM', dob1, 'Actress')
print(adult.birthday, adult.age, adult.profession)
adult.improvization()