from product import Product
from transaction import Transaction, TransactionItem
from shop import Shop


shop = Shop((Product("Pencil", 3000), Product("Book", 5000)))
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