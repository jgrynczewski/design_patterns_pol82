from lib import Product, Color, Size, ProductFilter


apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
for product in pf.filter_by_color(products, Color.GREEN):
    print(f"{product.name} is green.")

for product in pf.filter_by_size(products, Size.LARGE):
    print(f"{product.name} is large.")
