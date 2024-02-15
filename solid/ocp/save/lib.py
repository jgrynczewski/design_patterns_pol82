# Zachowajmy zasadę OCP
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Filter:
    def filter(self, products, specification):
        for p in products:
            if specification.is_satisfied(p):
                yield p
