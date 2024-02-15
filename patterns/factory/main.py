class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients


b = Burger(['wheat bean', 'beef', 'pickles', ...])


class BurgerFactory:
    def create_hamburger(self):
        ingredients = ['wheat bean', 'beef', 'pickles', ...]
        return Burger(ingredients)

    def create_mcrolay(self):
        ingredients = ['beef', 'cheddar', ...]
        return Burger(ingredients)


b2 = BurgerFactory().create_hamburger()