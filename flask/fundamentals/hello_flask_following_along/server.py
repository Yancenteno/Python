from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}'

@app.route('/hello/<name>/<food>')
def hello_name2(name,food):
    return f'Hello {name} favorite food is {food}!'

if __name__=="__main__":
    app.run(debug=True)  

