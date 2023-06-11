class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


products = (Product("Pencil", 3000), Product("Book", 5000))

for index, product in enumerate(products):
    print(str(index + 1) + ". " + product.name + " \tRp. "  + str(product.price))

option = int(input("Enter your option : "))

if (option < 1 or option > len(products)):
    print("Invalid option")
else:
    selectedProduct = products[option - 1]
    print("You choose " + selectedProduct.name + " with price Rp." + str(selectedProduct.price))

    amount = int(input("Enter amount : "))
    total = selectedProduct.price * amount

    print("Total price is Rp. " + str(total))
    
    money = int(input("Enter money : "))
    diff = money - total

    if (diff < 0):
        print("you need Rp. " + str(diff * -1) + " more money")
    elif (diff > 0):
        print("your change is Rp. " + str(diff))
    else:
        print("your money is enough")
