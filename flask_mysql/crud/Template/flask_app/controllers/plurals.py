from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models._____ import _____



@app.route('/')
def index():
    return redirect('/users')