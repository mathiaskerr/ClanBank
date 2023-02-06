from datetime import date
from models.user import User

class Transaction:
    def __init__(self, merchant, tag, amount, time, id=None):
        self.merchant = merchant
        self.tag = tag
        self.amount = amount
        self.time = time
        self.id = id

    # def total_amount(transactions):
    #     total = 0
    #     for transaction in transactions:
    #         total += transaction.amount
    #     return total    

    # def on_budget(budget, total):

    #     spend = budget - total
    #     if spend > 0:
    #         spending = f'You have £{spend} left.'
    #     else:
    #         spending = f'You have gone £{spend * -1} over.' 