from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá!"

@app.route('/about')
def about():
    return "Esta é uma API simples criada com Flask."
