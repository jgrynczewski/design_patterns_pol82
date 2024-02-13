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

    @staticmethod
    def get_circle_area(r):
        return 3.14 * r**2

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

result = c.get_circle_area(1)
print(result)
