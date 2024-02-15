from lib import Product, Color, Size, Filter
from specification.color_specification import ColorSpecification
from specification.size_specification import SizeSpecification

apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]
print("=== Nowa wersja ===")

f = Filter()
for product in f.filter(products, ColorSpecification(Color.GREEN)):
    print(f"{product.name} is green.")

f = Filter()
for product in f.filter(products, SizeSpecification(Size.LARGE)):
    print(f"{product.name} is large.")
