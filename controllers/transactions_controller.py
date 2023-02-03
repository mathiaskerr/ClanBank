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