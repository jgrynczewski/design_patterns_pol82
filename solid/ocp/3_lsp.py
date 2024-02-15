# LSP - Liskov Substitution Principle
import abc


class IAnimal:
    @property
    @abc.abstractmethod
    def num_legs(self) -> int:
        ...


class Lion(IAnimal):
    def __init__(self):
        self._num_legs = 4

    @property
    def num_legs(self):
        return self._num_legs


class Penquin(IAnimal):
    def __init__(self):
        self._num_legs = 2

    @property
    def num_legs(self):
        return self._num_legs


class Snake(IAnimal):
    def __init__(self):
        self._num_legs = 0

    @property
    def num_legs(self):
        return self._num_legs


class Herd:
    def __init__(self, animal, num_legs):
        self.animal = animal
        self.num_legs = num_legs

    def count_members(self):
        return int(self.num_legs / self.animal.num_legs)


l = Lion()
h = Herd(l, 100)
print(h.count_members())

p = Penquin()
h = Herd(p, 28)
print(h.count_members())

# # Złamanie zasady lsp
# s = Snake()
# h = Herd(s, 30)
# print(h.count_members())