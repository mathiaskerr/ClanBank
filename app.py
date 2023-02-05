from flask import Flask, render_template
from controllers.transactions_controller import transactions_blueprint
from controllers.merchants_controller import merchants_blueprint
from controllers.users_controller import users_blueprint
from repositories import transaction_repository
from repositories import user_repository

app = Flask(__name__)


app.register_blueprint(transactions_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    user = user_repository.select_all()
    user = user_repository.select(user[0].id)
    transactions = transaction_repository.select_all()
    total = 0
    for transaction in transactions:
        total += transaction.amount
    

    return render_template('index.html', total = total, user = user)

if __name__ == '__main__':
    app.run(debug=True)    