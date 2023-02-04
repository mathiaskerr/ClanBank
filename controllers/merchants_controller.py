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

# @merchants_blueprint.route("/merchants/new")
# def new_merchant():
#     return render_template("merchants/new.html")

@merchants_blueprint.route("/merchants", methods = ["POST"])
def create_merchant():
    name = request.form['name']
    category = request.form['category']
    merchant = Merchant(name, category)
    merchant_repository.save(merchant)
    return redirect('/merchants')

@merchants_blueprint.route("/<id>/edit_merchant")
def edit_merchant():
    merchant = merchant_repository.select(id)
    

@merchants_blueprint.route("/merchants/<id>/delete", methods = ["POST"])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect('/merchants')