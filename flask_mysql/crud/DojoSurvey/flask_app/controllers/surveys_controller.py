from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.survey_model import Survey



@app.route('/')
def reroute():
    return render_template("index.html")

@app.route('/survey', methods=['POST'])
def save_info():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/results')
    return redirect('/')

@app.route('/results')
def result():
    survey = Survey.get_recent()
    return render_template("result.html", survey = survey)
