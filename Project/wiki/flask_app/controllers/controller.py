from flask import render_template, redirect, request, session, flash
from flask_app import app

@app.route('/')
def start_page():
    return render_template('start.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/characters')
def friends():
    return render_template('characters.html')

@app.route('/location')
def family():
    return render_template('location.html')

@app.route('/episodes')
def enemies():
    return render_template('episodes.html')