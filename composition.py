# Kompozycja relacja typu HAS-A (ma) - krowa ma dzwonek (składa się z niego)

class Cow:
    def __init__(self, name, bell):
        self.name = name
        self.bell = bell

    # # krowa może być odpowiedzialna za stworzenie dzwonka
    # # wtedy będziemy mieli do czynienia z silniejszą kompozycją
    # def __init__(self, name, sound):
    #     self.name = name
    #     self.bell = Bell(sound)

    def ring_the_bell(self):
        self.bell.ring()


class Bell:
    def __init__(self, sound):
        self.sound = sound

    def ring(self):
        print(self.sound)


b1 = Bell("Ding Dong")
c = Cow("Mućka", b1)
c.ring_the_bell()

# # Silniejsza kompozycja
# # (krowa odpowiedzialna nie tylko za posiadanie dzwonka, ale również za jego tworzenie)
# c = Cow("Mućka", "Ding Dong")
