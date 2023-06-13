from product import Product

class TransactionItem:
    def __init__(self):
        self.product: Product | None = None
        self.amount = 0

    def getTotal(self):
        if (self.product):
            return self.product.price * self.amount
        else:
            return 0

class Transaction:
    def __init__(self):
        self.items: list[TransactionItem] = []
        self.money = 0
    
    def getTotal(self):
        total = 0
        for item in self.items:
            total += item.getTotal()
        return total

    def getChange(self):
        return self.money - self.getTotal()
    
    def addItem(self, item: TransactionItem):
        self.items.append(item)