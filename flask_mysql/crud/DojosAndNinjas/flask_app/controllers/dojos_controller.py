from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def users():
    all_dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos = all_dojos)

@app.route('/dojos/show/<int:id>')
def show(id):
    data = {"id":id}
    dojo = Dojo.get_one(data)
    ninja = Ninja.get_all(data)
    return render_template("show_dojos.html", ninja = ninja, dojo = dojo)

@app.route('/dojos/new',methods = ['POST'])
def new_dojo():
    Dojo.save(request.form)
    return redirect("/dojos")