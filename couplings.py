# Sprzężenia (couplings)
class Cow:
    def __init__(self, name, bell: 'Bell'):
        self.name = name
        self.bell = bell

    def ring_the_bell(self):
        self.bell.ring()


class Bell:
    def __init__(self, sound):
        self._sound = sound

    def ring(self):
        print(self._sound)


class Butcher:
    def __init__(self, name):
        self.name = name

    def play_with(self, cow: Cow):
        cow.bell.ring()


b1 = Bell("Ding Dong")
c = Cow("Mućka", b1)
butcher = Butcher("Hans")

butcher.play_with(c)
