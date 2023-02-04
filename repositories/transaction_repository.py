from db.run_sql import run_sql
import pdb
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, tag, amount, time) VALUES (%s, %s, %s ,%s) RETURNING *"
    values = [transaction.merchant.id, transaction.tag, transaction.amount, transaction.time]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        merchant = merchant_repository.select(result['merchant_id'])
        transaction = Transaction(merchant, result['tag'], result['amount'], result['time'], result['id'])
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(merchant, row['tag'], row['amount'], row['time'], row['id'])
        transactions.append(transaction)
    return transactions   


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (merchant_id, tag, amount, time) = (%s, %s, %s, %s) WHERE id= %s"
    values = [transaction.merchant.id, transaction.tag, transaction.amount, transaction.time, transaction.id]
    run_sql(sql, values)

