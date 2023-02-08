from datetime import date
from models.user import User

class Transaction:
    def __init__(self, merchant, tag, amount, date, id=None):
        self.merchant = merchant
        self.tag = tag
        self.amount = amount
        self.date = date
        self.id = id
