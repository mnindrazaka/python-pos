class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Transaction:
    def __init__(self):
        self.product = None
        self.amount = 0
        self.money = 0
    
    def getTotal(self):
        return self.product.price * self.amount

    def getChange(self):
        return self.money - self.getTotal()
        

class Shop:
    def __init__(self, products):
        self.products = products
    
    def printProducts(self):
        for index, product in enumerate(self.products):
            print(str(index + 1) + ". " + product.name + " \tRp. "  + str(product.price))
    
    def getProductByOption(self, option):
        return self.products[option - 1]

    def isOptionValid(self, option):
        return option < 1 or option > len(self.products)
    


products = (Product("Pencil", 3000), Product("Book", 5000))

shop = Shop(products)
shop.printProducts()

option = int(input("Enter your option : "))

if (shop.isOptionValid(option)):
    transaction = Transaction()
    
    transaction.product = shop.getProductByOption(option)

    print("You choose " + transaction.product.name + " with price Rp." + str(transaction.product.price))

    transaction.amount = int(input("Enter amount : "))

    print("Total price is Rp. " + str(transaction.getTotal()))
    
    transaction.money = int(input("Enter money : "))

    if (transaction.getChange() < 0):
        print("you need Rp. " + str(transaction.getChange() * -1) + " more money")
    elif (transaction.getChange() > 0):
        print("your change is Rp. " + str(transaction.getChange()))
    else:
        print("your money is enough")
else:
    print("Invalid option")