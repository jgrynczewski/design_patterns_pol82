# Dziedziczenie (inheritance) to realizacja zasady DRY w obiektówce
# Dziedziczenie = relacja typu IS-A (jest) - krowa JEST zwierzęciem, Horse IS-A Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Witam, jestem {self.name}")


class Cow(Animal):
    def __init__(self, name, is_alive):
        super().__init__(name)
        self.is_alive = is_alive

    # Krowa dziedziczy metodę rodzica - speak


class Horse(Animal):
    # Koń nadpisuje metodę rodzica - speak
    def speak(self):
        print(f"Ihahahaha, nazywam się {self.name}")


class Turtle(Animal):
    # żółw rozbudowuje metodę rodzica - speak
    def speak(self):
        super().speak()
        print("i jestem żółwiem.")


c = Cow("Mućka", is_alive=True)
c.speak()

h = Horse("Horacy")
h.speak()

t = Turtle("Michellangelo")
t.speak()
