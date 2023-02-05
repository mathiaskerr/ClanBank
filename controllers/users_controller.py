from flask import Flask, render_template, request, redirect
from repositories import user_repository
from models.user import User

from flask import Blueprint

users_blueprint = Blueprint("users",__name__)

@users_blueprint.route("/profile")
def user():
    users = user_repository.select_all()
    return render_template("users/index.html", users=users)

@users_blueprint.route("/profile/<id>/edit")
def edit_user(id):
    user = user_repository.select(id)
    return render_template("users/edit.html", user=user)

@users_blueprint.route("/profile/<id>/update", methods = ['POST'])
def update_user(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    budget = request.form['budget']
    user = User(first_name, last_name, budget, id)
    user_repository.update(user)
    return redirect('/profile')

