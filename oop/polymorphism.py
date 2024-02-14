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

# ========================================================================

def sing(animal):
    animal.speak()


zoo = [Cow(), Horse(), Dog()]
for animal in zoo:
    sing(animal)
