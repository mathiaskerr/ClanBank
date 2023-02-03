from db.run_sql import run_sql
import pdb
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, tag, amount, time) VALUES (%s, %s, %s ,%s) RETURNING *"
    values = [transaction.merchant.id, transaction.tag, transaction.amount, transaction.time]
    results = run_sql(sql, values)
    # pdb.set_trace()
    id = results[0]['id']
    transaction.id = id
    return transaction