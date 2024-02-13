# Przykład zastosowania metod klasowych
# alternatywna konstrukcja obiektu (metoda fabrykująca)
# domyślny konstruktor - __new__

class Cow:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive

    # metoda fabrykująca
    @classmethod
    def create_alive_cow(cls, name):
        obj = cls(name, is_alive=True)
        return obj


# To jest stworzenie obiektu klasy krowa
c = Cow("Mućka", True)

# To też jest stworzenie obiektu klasy krowa
c2 = Cow.create_alive_cow("Milka")

print(c.name)
print(c2.name)
