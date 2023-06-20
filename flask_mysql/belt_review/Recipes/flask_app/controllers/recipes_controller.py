from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


@app.route('/recipes/new')
def new_recipes():
    
    return render_template('new_recipes.html')


@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    
    recipe_data = {
        **request.form, 
        'user_id' : session['user_id']
    }
    
    Recipe.save_recipe(recipe_data)
    
    return redirect('/recipes')


@app.route('/show/<int:recipe_id>')
def show_recipe(recipe_id):
    one_recipe = Recipe.get_one_recipe({'recipe_id' : recipe_id})
    
    newUser = User.get_id({'user_id': session['user_id']})
    
    return render_template("show.html", one_recipe = one_recipe, newUser=newUser)


@app.route('/recipes/edit/<int:recipe_id>')
def edit(recipe_id):
    one_recipe = Recipe.get_one_recipe({'recipe_id' : recipe_id})
    
    return render_template('edit_recipe.html', one_recipe = one_recipe)



@app.route('/recipe/update/<int:recipe_id>', methods=['POST'])
def updated(recipe_id):
    
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{recipe_id}')
    
    Recipe.update_recipe({
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date' : request.form['date'],
        'under_30' : request.form['under_30'],
        'recipe_id' : recipe_id
    })
    
    return redirect('/recipes')



@app.route('/recipes/delete/<int:recipe_id>')
def delete(recipe_id):
    Recipe.delete_recipe({'recipe_id' : recipe_id})
    return redirect('/recipes')