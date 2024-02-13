# polimorfizm - wielopostaciowość
# typowanie statyczne
# typowanie dynamiczne (statyczne, behiaworalne, duck typing)
class Animal:
    def speak(self):
        pass


class Cow(Animal):
    def speak(self):
        print("Muuuuuuuu")


class Horse(Animal):
    def speak(self):
        print("Ihahahahaha")


class Dog(Animal):
    def speak(self):
        print("Hauhauhau")


def sing(animal):
    animal.speak()


zoo = [Cow(), Horse(), Dog()]
for animal in zoo:
    sing(animal)
