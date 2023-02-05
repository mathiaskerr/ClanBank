from db.run_sql import run_sql

from models.user import User


def save(user):
    sql = "INSERT INTO users (first_name, last_name, budget) VALUES (%s, %s, %s) RETURNING *"
    values = [user.first_name, user.last_name, user.budget]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def delete_all():
    sql = "DELETE  FROM users"
    run_sql(sql)

def update(user):
    sql = "UPDATE users SET (first_name, last_name, budget) = (%s, %s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.budget, user.id]
    run_sql(sql, values)