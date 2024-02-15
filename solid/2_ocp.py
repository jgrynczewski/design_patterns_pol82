# OCP - Open-Close Principle
import abc
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


# Łamiemy zasadę OCP
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p


apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
for product in pf.filter_by_color(products, Color.GREEN):
    print(f"{product.name} is green.")

for product in pf.filter_by_size(products, Size.LARGE):
    print(f"{product.name} is large.")


# Zachowajmy zasadę OCP
class ISpecification(abc.ABC):
    @abc.abstractmethod
    def is_satisfied(self, item: Product) -> bool:
        ...


class ColorSpecification(ISpecification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(ISpecification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class Filter:
    def filter(self, products, specification: ISpecification):
        for p in products:
            if specification.is_satisfied(p):
                yield p


print("=== Nowa wersja ===")
f = Filter()
for product in f.filter(products, ColorSpecification(Color.GREEN)):
    print(f"{product.name} is green.")
