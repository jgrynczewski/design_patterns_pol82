# Sprzężenia (couplings)
class Cow:
    def __init__(self, name, bell):
        self.name = name
        self.bell = bell

    def ring_the_bell(self):
        self.bell.ring()


class Bell:
    def __init__(self, sound):
        self.voice = sound

    def ring(self):
        print(self.voice)


class Butcher:
    def __init__(self, name):
        self.name = name

    def play_with(self, cow):
        cow.ring_the_bell()


b1 = Bell("Ding Dong")
c = Cow("Mućka", b1)
butcher = Butcher("Hans")

butcher.play_with(c)
