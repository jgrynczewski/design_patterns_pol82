# modyfikatory dostępu
# w praktyce, w pythonie:
# field - składowa publiczna  - wchodź, tutaj jesteś bezpieczny
# _field - składowa chroniona  -  wchodzisz na własną odpowiedzialność, zachowaj szczególną ostrożność
# __field - składowa prywatna  -  wstęp surowa wzbroniony

# w teorii:
# field - składowa publiczna widoczna jest wszędzie
# _field - składowa chroniona widoczna jest w swojej klasie i we wszystkich klasach po niej dziedziczących
# __field - składowa prywatna widoczna jest wyłącznie w swojej klasie

class Account:
    def __init__(self, amount):
        self._amount = amount


a = Account(100)

# składowe prywatne - name mangling
# print(a.__amount)
# print(a._Account__amount)
