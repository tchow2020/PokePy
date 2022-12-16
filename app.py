from models.pokemon import Pokemon
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Pokemon.GetPokemon, ('/Pokemon/find/<string:name>'))
api.add_resource(Pokemon.Abilites, ('/Pokemon/abilities/<int:tipo>'))

if __name__ == '__main__':
    app.run(debug=True)