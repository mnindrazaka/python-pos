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