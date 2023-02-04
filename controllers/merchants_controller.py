from flask import Flask, render_template, request, redirect
from repositories import transaction_repository
from repositories import merchant_repository
from models.merchant import Merchant

from flask import Blueprint

merchants_blueprint = Blueprint("merchants",__name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", all_merchants = merchants)