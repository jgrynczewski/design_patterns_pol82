# gettery i settery zapewniają nam kontrolę dostępu do atrybutów
class Account:
    def __init__(self, amount):
        self._amount = amount

    # getter
    def get_amount(self):
        return self._amount

    #setter
    def set_amount(self, new_amount):
        if type(new_amount) in [int, float] and new_amount > 0:
            self._amount = new_amount


a = Account(100)
print(a.get_amount())
a.set_amount(1000)
print(a.get_amount())
a.set_amount(-100)
print(a.get_amount())
a.set_amount("Ala ma kota")
print(a.get_amount())


# property
# kontrolowany dostęp przy jednoczesnym zachowaniu zwięzłej notacji
class Account2:
    def __init__(self, amount):
        self._amount = amount

    # getter
    def get_amount(self):
        return self._amount

    #setter
    def set_amount(self, new_amount):
        if type(new_amount) in [int, float] and new_amount > 0:
            self._amount = new_amount

    amount = property(get_amount, set_amount)


print("=======================")
a = Account2(100)
print(a.amount)
a.amount = "Ala ma kota"
print(a.amount)
a.amount = 500
print(a.amount)


# syntactic sugare (cukier syntaktyczny)
class Account3:
    def __init__(self, amount):
        self._amount = amount

    # getter
    @property
    def amount(self):
        return self._amount

    #setter
    @amount.setter
    def amount(self, new_amount):
        if type(new_amount) in [int, float] and new_amount > 0:
            self._amount = new_amount
