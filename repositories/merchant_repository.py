from db.run_sql import run_sql

from models.merchant import Merchant
from models.transaction import Transaction

def save(merchant):
    sql = "INSERT INTO merchants (name, category) VALUES (%s, %s) RETURNING *"
    values = (merchant.name, merchant.category)
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        merchant = Merchant(result['name'], result['category'], result['id'])
    return merchant    

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['category'], row['id'])
        merchants.append(merchant)
    return merchants    

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    sql = "UPDATE merchants SET (name, category) = (%s, %s) WHERE id = %s"
    values = [merchant.name, merchant.category, merchant.id]
    run_sql(sql, values)

def transactions(merchant):
    transactions = []
    sql = "SELECT * FROM transactions WHERE merchant_id = %s"
    values = [merchant.id]
    results = run_sql(sql, values)

    for row in results:
        transaction = Transaction(merchant, row['tag'], row['amount'], row["time"], row['id'])
        transactions.append(transaction)
    return transactions