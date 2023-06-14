from flask import Flask, render_template, request, redirect, session


from flask_app.models.game_model import Game


@app.route('/game_form')
def show_form():
    
    return render_template('game_form.html')
    
    
@app.route('/submit_game_form', methods=['POST'])
def submit_game_form():
    
    data = {
        'name' : request.form['name'],
        'genre' : request.form['genre'],
        'release_year' : request.form['release_year']
    }
    
    Game.add_games(data)
    
    return redirect('/')


@app.route('/')
def Home():
    
    all_games = Game.get_all()
    print(all_games)
    return render_template('index.html', all_games = all_games)


@app.route('/edit/<int:game_id>')
def show_edit_form(game_id):
    
    Game.get_one({{game_id : game_id}})
    
    return render_template('edit_form.html', one_game=one_game)






if __name__ == "__main__":
    app.run(debug=True)