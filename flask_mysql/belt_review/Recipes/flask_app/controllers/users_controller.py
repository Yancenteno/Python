from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt  = Bcrypt(app)

@app.route('/')
def account():
    return render_template('index.html')

@app.route('/recipes/<int:user_id>')
def user(user_id):
    if 'user_id' not in session:
        return redirect('/')
    
    newUser = User.get_id({'user_id': user_id})
    
    return render_template('recipes.html', newUser = newUser)

@app.route('/login', methods = ['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    print(user_in_db)
    if not user_in_db:
        flash('Invalid Email/Password')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password')
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    
    return redirect(f'/recipes/{user_in_db.id}')


@app.route('/register', methods = ['POST'])
def register():
    if not User.validate_account(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
    
    user_id = User.save(data)
    
    session['user_id'] = user_id
    
    return redirect(f'/recipes/{user_id}')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname


# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================


# ====================================
# Log In Validations Route
# ====================================


# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================


# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================


# ====================================
#    Delete Routes
# ====================================