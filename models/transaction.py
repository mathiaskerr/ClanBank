from datetime import datetime

class Transaction:
    def __init__(self, merchant, tag, amount, time, id=None):
        self.merchant = merchant
        self.tag = tag
        self.amount = amount
        self.time = time
        self.id = id

    def total_amount(transactions):
        total = 0
        for transaction in transactions:
            total += transaction.amount
        return total    
