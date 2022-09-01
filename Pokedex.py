from flask import Flask, render_template
from requests import request

app=Flask(__name__)

# fazendo conexão com a tela
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)