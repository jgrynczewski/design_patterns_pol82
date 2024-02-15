import abc


class IFlyable(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        ...


class FlyWithWings(IFlyable):
    def fly(self):
        print("Latam")


class FlyNoWay(IFlyable):
    def fly(self):
        print("Nic nie robię")


class IQuackable(abc.ABC):
    @abc.abstractmethod
    def quack(self):
        ...


class Quack(IQuackable):
    def quack(self):
        print("Kwa kwa")


class Squack(IQuackable):
    def quack(self):
        print("Piszczę")


class QuackNoWay(IQuackable):
    def quack(self):
        print("Nic nie robię")


#### Dziedzieczenie vs Kompozycja - ostateczne starcie
class Duck(abc.ABC):
    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    @abc.abstractmethod
    def __str__(self):
        ...


class WildDuck(Duck):
    def __init__(self):
        self.quack_behavior: IQuackable = Quack()
        self.fly_behavior: IFlyable = FlyWithWings()

    def __str__(self):
        return "Jestem kaczką krzyżówką"


######################

quack = WildDuck()

quack.perform_quack()
quack.perform_fly()

quack.quack_behavior = QuackNoWay()
quack.perform_quack()
