from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninjas')
def new():
    all_dojos = Dojo.get_all()
    return render_template("ninjas.html", all_dojos = all_dojos)

@app.route('/new_ninja',methods=['POST'])
def new_ninja():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect("/dojos")