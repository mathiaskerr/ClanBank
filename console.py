import pdb
from models.merchant import Merchant
from models.transaction import Transaction
from models.user import User

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

merchant_repository.delete_all()
transaction_repository.delete_all()
user_repository.delete_all()

merchant_1 = Merchant('Lidl', "grocery")
merchant_2 = Merchant('Tesco', 'Grocery')
merchant_3 = Merchant('Howlin Wolf', 'Bar')

user_1 = User("Mathias", "Kerr", 1000.50)
user_repository.save(user_1)

merchant_repository.save(merchant_1)
merchant_repository.save(merchant_2)
merchant_repository.save(merchant_3)
# result = merchant_repository.select(2)
# result = merchant_repository.select_all()
# merchant_repository.delete(19)

transaction_1 = Transaction(merchant_1, 'Weekly Shop', 50.50, '14:15')
transaction_2 = Transaction(merchant_2, 'Alcohol', 35.50, '12:00')
transaction_3 = Transaction(merchant_3, 'Food' , 14.00, '21:50')
# transaction_repository.delete(40)
transaction_repository.save(transaction_1)
transaction_repository.save(transaction_2)
transaction_repository.save(transaction_3)
# result1 = transaction_repository.select_all()


# pdb.set_trace()