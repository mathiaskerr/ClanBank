from datetime import datetime

class Transaction:
    def __init__(self, merchant, tag, amount, time, id=None):
        self.merchant = merchant
        self.tag = tag
        self.amount = amount
        self.time = time
        self.id = id

        # datetime.now()