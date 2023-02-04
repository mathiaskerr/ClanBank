import pdb
from flask import Flask, render_template, request, redirect
from repositories import transaction_repository
from repositories import merchant_repository
from models.transaction import Transaction

from flask import Blueprint

transactions_blueprint = Blueprint("transactions",__name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", all_transactions = transactions) 

@transactions_blueprint.route("/transactions/new")
def new_transaction():
    merchants = merchant_repository.select_all()
    return render_template("transactions/new.html", all_merchants = merchants)

@transactions_blueprint.route("/transactions", methods = ["POST"])
def create_transaction():
    merchant_id = request.form['merchant_id']
    tag = request.form['tag']
    time = request.form['time']
    amount = request.form['amount']
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(merchant, tag, amount, time)
    transaction_repository.save(transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transaction/<id>")
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template("transactions/show.html", show_transaction = transaction)

@transactions_blueprint.route("/<id>/edit_transaction")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    return render_template("transactions/edit.html", transaction = transaction, merchants = merchants)

@transactions_blueprint.route("/transaction/<id>/delete", methods = ["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')