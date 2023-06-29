from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User

@app.route('/')
def start_page():
    return render_template('start.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/')
    
    newUser = User.get_id({'user_id': session['user_id']})
    
    return render_template('home.html', newUser=newUser)



@app.route('/characters')
def characters():
    if 'user_id' not in session:
        return redirect('/')
    
    newUser = User.get_id({'user_id': session['user_id']})
    
    return render_template('characters.html', newUser=newUser)



@app.route('/location')
def location():
    if 'user_id' not in session:
        return redirect('/')
    
    newUser = User.get_id({'user_id': session['user_id']})
    
    return render_template('location.html', newUser=newUser)



@app.route('/episodes')
def episodes():
    if 'user_id' not in session:
        return redirect('/')
    
    newUser = User.get_id({'user_id': session['user_id']})
    
    return render_template('episodes.html', newUser=newUser)



@app.route('/dead')
def dead():
    if 'user_id' not in session:
        return redirect('/')
    
    newUser = User.get_id({'user_id': session['user_id']})
    
    return render_template('dead.html', newUser=newUser)



@app.route('/alive')
def alive():
    if 'user_id' not in session:
        return redirect('/')
    
    newUser = User.get_id({'user_id': session['user_id']})
    
    return render_template('alive.html', newUser=newUser)