# polimorfizm - wielopostaciowość
# typowanie statyczne (aka nominalne)
# typowanie dynamiczne (strukturalne, behawioralne, duck typing)

# interfejs - relacja typu IMPLEMENT (implementuje)
import abc


class IAnimal(abc.ABC):

    @abc.abstractmethod
    def speak(self):
        """Abstract method speak"""


class Cow(IAnimal):
    def speak(self):
        print("Muuuuuuuu")


class Horse(IAnimal):
    def speak(self):
        print("Ihahahahaha")


class Dog(IAnimal):
    def speak(self):
        print("Hauhauhau")


class Context:
    def sing(animal: IAnimal) -> None:
        animal.speak()


# ================================================


zoo = [Cow(), Horse(), Dog()]
c = Context()
for animal in zoo:
    c.sing(animal)
