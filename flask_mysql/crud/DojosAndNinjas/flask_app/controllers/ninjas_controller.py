from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


# @app.route('/')
# def index():
#     return redirect('/ninjas')

# @app.route('/ninjas')
# def users():
#     return render_template("ninjas.html", ninjas = Ninja.get_all())

# @app.route('/ninjas/new')
# def new():
#     return render_template("new_ninjas.html")

# @app.route('/ninjas/create', methods=['Post'])
# def create():
#     print(request.form)
#     Ninja.save(request.form)
#     return redirect('/ninjas')

# @app.route('/ninjas/edit/<int:id>')
# def edit(id):
#     data = {
#         "id":id
#     }
#     return render_template("edit_ninjas.html", ninjas = Ninja.get_one(data))

# @app.route('/ninjas/show/<int:id>')
# def show(id):
#     data = {
#         "id":id
#     }
#     return render_template("show_ninjas.html", ninja = Ninja.get_one(data))

# @app.route('/ninjas/update', methods = ['POST'])
# def update():
#     Ninja.update(request.form)
#     return redirect('/ninjas')

# @app.route('/ninjas/delete/<int:id>')
# def delete(id):
#     data = {
#         "id":id
#     }
#     Ninja.delete(data)
#     return redirect('/ninja')