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

merchant_1 = Merchant('UK Government', "Espionage")
merchant_2 = Merchant('Jaguar', 'Automobile')
merchant_3 = Merchant('Love Honey', '****')

user_1 = User("Austin", "Powers", 1000.00)
result = user_repository.save(user_1)


merchant_repository.save(merchant_1)
merchant_repository.save(merchant_2)
merchant_repository.save(merchant_3)
# result = merchant_repository.select(2)
# result = merchant_repository.select_all()
# merchant_repository.delete(19)

transaction_1 = Transaction(merchant_1, 'Guns', 45000, '14:15')
transaction_2 = Transaction(merchant_2, 'Shaguar', 60000, '12:00')
transaction_3 = Transaction(merchant_3, 'Love Honey' , 69.00, '21:50')
# transaction_repository.delete(40)
transaction_repository.save(transaction_1)
transaction_repository.save(transaction_2)
transaction_repository.save(transaction_3)
# result1 = transaction_repository.select_all()


pdb.set_trace()