from product import Product

class Shop:
    def __init__(self, products: list[Product]):
        self.products = products
    
    def printProducts(self):
        for index, product in enumerate(self.products):
            print(str(index + 1) + ". " + product.name + " \tRp. "  + str(product.price))
    
    def getProductByOption(self, option: int):
        return self.products[option - 1]

    def isOptionValid(self, option: int):
        return option > 0 and option <= len(self.products)