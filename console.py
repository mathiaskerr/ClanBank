import pdb
from models.merchant import Merchant
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

# merchant_repository.delete_all()

merchant_1 = Merchant('Lidl', "grocery")
merchant_2 = Merchant('Tesco', 'Grocery')

# merchant_repository.save(merchant_1)
# merchant_repository.save(merchant_2)
# result = merchant_repository.select(13)
# result = merchant_repository.select_all()
# merchant_repository.delete(19)

transaction_1 = Transaction(merchant_1, 'Weekly Shop', 50.50, '14:15')
transaction_2 = Transaction(merchant_2, 'Alcohol', 35.50, '12:00')

# result = transaction_repository.save(transaction_1)

pdb.set_trace()