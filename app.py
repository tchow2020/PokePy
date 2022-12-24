from models.pokemon import Pokemon
from models.pokemonf import PokemonF
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_restful import Api

app = Flask(__name__)
# api = Api(app)

# api.add_resource(Pokemon.GetPokemon, ('/Pokemon/find/<string:name>'))
# api.add_resource(Pokemon.Homologação, ('/Pokemon/Homologação'))


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', listPokemon = PokemonF.getAllPokemon(), listAll = True)
    if request.method == 'POST':
        return render_template('index.html', listPokemon = PokemonF.getPokemon(request.form['nome']))

if __name__ == '__main__':
    app.run(debug=True)
