from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def save_info():
    session['username'] = request.form['name']
    session['locationchoice'] = request.form['location']
    session['languagechoice'] = request.form['language']
    session['message'] = request.form['comment']
    return redirect("/result")

@app.route('/result')
def show_info():
    return render_template("result.html", name_on_template=session['username'], location_on_template=session['locationchoice'], language_on_template=session['languagechoice'], comment_on_template=session['message'])





if __name__=="__main__":
    app.run(debug=True)

