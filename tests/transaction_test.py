import unittest

from models.transaction import Transaction 
from models.merchant import Merchant
import datetime


class TestTransaction(unittest.TestCase):
    
    def setUp(self):
        self.merchant_1 = Merchant('UK Government', "Espionage", True)
        self.merchant_2 = Merchant('Jaguar', 'Automobile', True)
        self.merchant_3 = Merchant('Love Honey', '****', True)


        self.transaction_1 = Transaction(self.merchant_1, 'Guns', 45000, datetime.date(2023,1,1))
        self.transaction_2 = Transaction(self.merchant_2, 'Shaguar', 60000, datetime.date(2022,12,26))
        self.transaction_3 = Transaction(self.merchant_3, 'Love Honey' , 69.00, datetime.date(2023,2,1))

        self.transactions = [self.transaction_1, self.transaction_2, self.transaction_3]

        def test_total_spend(self):
            self.transaction.total_spend(self.transactions)
            self.assertEqual(105069, self.transaction.total_spend(self.transactions))

        def test_transaction_by_tag(self):
            transaction_tag = self.transaction.transaction_by_tag(self.transaction_1.tag, self.transactions)
            self.assertEqual(1, len(transaction_tag))


