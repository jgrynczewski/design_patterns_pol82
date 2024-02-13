# Zależność (dependency) - relacja typu USE-A (używa)
class Cow:
    def __init__(self, name):
        self.name = name

    def ring_the_bell(self, bell):
        bell.ring()


class Bell:
    def __init__(self, sound):
        self.sound = sound

    def ring(self):
        print(self.sound)


b = Bell("Ding Dong")
c = Cow("Mućka")

c.ring_the_bell(b)


# dependency injection (wstrzykiwanie zależności)
