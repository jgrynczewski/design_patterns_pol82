import abc


class Duck(abc.ABC):
    def quack(self):
        print("Kwa kwa")

    def swim(self):
        print("Pływam")

    def fly(self):
        print("Latam")

    @abc.abstractmethod
    def __str__(self):
        ...


class WildDuck(Duck):
    def __str__(self):
        return "Jestem kaczką krzyżówką."


class Shoveler(Duck):
    def __str__(self):
        return "Jestem kaczką płaskonos."


class RubberDuck(Duck):
    def quack(self):
        print("Piszczę")

    def fly(self):
        print("Nie robię nic")

    def __str__(self):
        return "Jestem gumową kaczką"


class WoodenDuck(Duck):
    def quck(self):
        print("Nie robię nic")

    def fly(self):
        print("Nie robię nic")

    def __str__(self):
        return "Jestem drewnianą kaczką"
