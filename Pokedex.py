from unittest import result
from urllib import request
from flask.globals import request 
from flask import Flask, render_template
import requests
import json

from models.pokemon import Pokemon

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Buscar', methods=['GET', 'POST'])
def buscar():
    pokemon = Pokemon(request.form['nome'].lower(),'')
    try:
        res = json.loads(request.get('https://pokeapi.co/api/v2/pokemon/{pokemon.name}'))
        result = res['sprites']
        result = result['front_default']
        pokemon.foto = result 
    except:
        return 'Pokemon não encontrado'

    return render_template('index.html', 
    nome = pokemon.nome,
    foto = pokemon.foto,
    
    )

if __name__ == '__main__':
    app.run(debug=True)