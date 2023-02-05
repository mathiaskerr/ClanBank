from db.run_sql import run_sql

from models.user import User


def save(user):
    sql = "INSERT INTO users (first_name, last_name, budget) VALUES (%s, %s, %s) RETURNING *"
    values = [user.first_name, user.last_name, user.budget]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['first_name'], row['last_name'], row['budget'], row['id'] )
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM USERS WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        user = User(result['first_name'], result['last_name'], result['budget'], result['id'])
    return user    

def delete_all():
    sql = "DELETE  FROM users"
    run_sql(sql)

def update(user):
    sql = "UPDATE users SET (first_name, last_name, budget) = (%s, %s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.budget, user.id]
    run_sql(sql, values)