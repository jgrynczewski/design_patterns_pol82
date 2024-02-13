# DRY - Don't repeat yourself

class Cow:
    # atrybut klasowy
    species = "mammals"

    def __init__(self, name):
        # atrybuty obiektowe
        self.name = name
        self.is_alive = True

    # metody obiektowy
    def speak(self):
        print(f"Muuuuu. Cześć nazywam się {self.name}")

    def kill_yourself(self):
        self.is_alive = False

    # metoda klasowa
    @classmethod
    def change_species(cls):
        cls.species = "bird"


c = Cow("Mućka")
c.speak()

c2 = Cow("Milka")
c2.speak()

Cow.change_species()
print(c.species)
