from flask import render_template, redirect, request, session, flash
from flask_app import app

@app.route('/')
def start_page():
    return render_template('start.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/episodes')
def episodes():
    return render_template('episodes.html')

@app.route('/dead')
def dead():
    return render_template('dead.html')

@app.route('/alive')
def alive():
    return render_template('alive.html')