class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TransactionItem:
    def __init__(self):
        self.product = None
        self.amount = 0

    def getTotal(self):
        return self.product.price * self.amount

class Transaction:
    def __init__(self):
        self.items = []
        self.money = 0
    
    def getTotal(self):
        total = 0
        for item in self.items:
            total += item.getTotal()
        return total

    def getChange(self):
        return self.money - self.getTotal()
    
    def addItem(self, item):
        self.items.append(item)

class Shop:
    def __init__(self, products):
        self.products = products
    
    def printProducts(self):
        for index, product in enumerate(self.products):
            print(str(index + 1) + ". " + product.name + " \tRp. "  + str(product.price))
    
    def getProductByOption(self, option):
        return self.products[option - 1]

    def isOptionValid(self, option):
        return option > 0 and option <= len(self.products)
    


products = (Product("Pencil", 3000), Product("Book", 5000))

shop = Shop(products)
transaction = Transaction()


isAddItem = True

while isAddItem:
    shop.printProducts()
    
    option = 0
    while True:
        option = int(input("Enter your option : "))
        if (shop.isOptionValid(option)):
            break
        else:
            print("Invalid option")

    item = TransactionItem()
    item.product = shop.getProductByOption(option)
    print("You choose " + item.product.name + " with price Rp." + str(item.product.price))
    item.amount = int(input("Enter amount : "))
    transaction.addItem(item)
    print("Now you need to pay Rp. " + str(transaction.getTotal() )) 
        
    isAddItem = input("Add more item (y/n) ? ").lower() == "y"

while True:
    transaction.money = int(input("Enter money : "))
    if transaction.getChange() >= 0:
        break
    else:
        print("you need Rp. " + str(transaction.getChange() * -1) + " more money")
    
if (transaction.getChange() > 0):
    print("your change is Rp. " + str(transaction.getChange()))
else:
    print("your money is enough")