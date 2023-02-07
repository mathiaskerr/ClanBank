from flask import Flask, render_template, request, redirect
from repositories import transaction_repository
from repositories import merchant_repository
from repositories import user_repository
from models.transaction import Transaction
from models.user import User
from models.functions import *
from datetime import datetime, date
from flask import Blueprint

transactions_blueprint = Blueprint("transactions",__name__)
# ive done this in a bit of a messy way but I believe if there was multiple users it would be easier to clean up
@transactions_blueprint.route("/transactions")
def transactions():
    user = user_repository.select_all()
    user = user_repository.select(user[0].id)
    transactions = transaction_repository.select_all()
    transactions.sort(key=lambda r: r.date)
    transactions.reverse()
    total = total_spend(transactions)
    spending = over_under_budget(user.budget, total)
    return render_template("transactions/index.html", all_transactions=transactions, user=user, total=total, spending=spending ) 


@transactions_blueprint.route("/transactions/new")
def new_transaction():
    merchants = merchant_repository.select_all()
    return render_template("transactions/new.html", all_merchants = merchants)

@transactions_blueprint.route("/transactions", methods = ["POST"])
def create_transaction():
    merchant_id = request.form['merchant_id']
    tag = request.form['tag']
    tag = tag.upper()
    date = datetime.strptime(request.form["date"], '%Y-%m-%d')
    date = datetime.date(date)
    amount = request.form['amount']
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(merchant, tag, amount, date)
    transaction_repository.save(transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transaction/<id>")
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template("transactions/show.html", show_transaction = transaction)

@transactions_blueprint.route("/<id>")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    return render_template("transactions/edit.html", transaction = transaction, merchants = merchants)

@transactions_blueprint.route("/transaction/<id>/edit", methods = ['POST'])
def update_transaction(id):
    merchant_id = request.form['merchant_id']
    tag = request.form['tag']
    tag = tag.upper()
    date = datetime.strptime(request.form["date"], '%Y-%m-%d')
    date = datetime.date(date)
    amount = request.form['amount']
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(merchant, tag, amount, date, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')   

@transactions_blueprint.route("/transaction/<id>/delete", methods = ["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')

@transactions_blueprint.route("/tags")
def tags():
    transactions = transaction_repository.select_all()
    tags= tags_index(transactions)
    return render_template("transactions/tags.html", tags = tags)

@transactions_blueprint.route("/tags/<tag>/transactions")
def tag_transactions(tag):
    transactions = transaction_repository.select_all()
    transaction_tag = transaction_by_tag(tag, transactions)
    total = total_spend(transaction_tag)
    return render_template("transactions/tag_transactions.html", transactions=transaction_tag, total=total)



