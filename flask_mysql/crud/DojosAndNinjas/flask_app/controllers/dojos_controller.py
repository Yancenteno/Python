from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def users():
    return render_template("dojos.html", dojos = Dojo.get_all())

@app.route('/dojos/new')
def new():
    return render_template("new_dojos.html")

@app.route('/dojos/create', methods=['Post'])
def create():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit_dojos.html", dojos = Dojo.get_one(data))

@app.route('/dojos/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template("show_dojos.html", dojos = Dojo.get_one(data))

@app.route('/dojos/update', methods = ['POST'])
def update():
    Dojo.update(request.form)
    return redirect('/dojos')

@app.route('/dojos/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    Dojo.delete(data)
    return redirect('/dojos')