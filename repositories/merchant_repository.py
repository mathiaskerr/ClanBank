from db.run_sql import run_sql

from models.merchant import Merchant
from models.transaction import Transaction

def save(merchant):
    sql = "INSERT INTO merchants (name, category, active) VALUES (%s, %s, %s) RETURNING *"
    values = (merchant.name, merchant.category, merchant.active)
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        merchant = Merchant(result['name'], result['category'], result['active'], result['id'])
    return merchant    

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['category'], row['active'], row['id'])
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
    sql = "UPDATE merchants SET (name, category, active) = (%s, %s, %s) WHERE id = %s"
    values = [merchant.name, merchant.category, merchant.active, merchant.id]
    run_sql(sql, values)

def transactions(id):
    transactions = []
    sql = "SELECT * FROM transactions WHERE merchant_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        merchant = select(id)
        transaction = Transaction(merchant, row['tag'], row['amount'], row["date"], row['id'])
        transactions.append(transaction)
    return transactions