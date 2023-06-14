from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key= "support dif"

from game_model import Game


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
    
    Game.add_game(request.form)
    
    return redirect('/')


@app.route('/')
def Home():
    
    all_games = Game.get_all()
    print(all_games)
    return render_template('index.html', all_games = all_games)







if __name__ == "__main__":
    app.run(debug=True)