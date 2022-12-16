from flask_restful import Resource
import requests

class Pokemon(Resource):
    def get(self):
        result = requests.get('https://pokeapi.co/api/v2/pokemon')
        dados = result.json()
        return dados["results"]

    class GetPokemon(Resource):
        def get(self, name):
            name = name.lower()
            result = requests.get('https://pokeapi.co/api/v2/pokemon/?&limit=1154')
            dados = result.json()
            listarPokemon = dados["results"]
            for pokemon in listarPokemon:
                if pokemon["name"] == name:
                    return pokemon
            
            return { 
                'error': True,
                'msg': 'Não identifiquei este pokemon'
            }
        
    class Abilites(Resource):
        def get(self, tipo):
            result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{tipo}/')
            dados = result.json()
            jsonReturn = {
                "nome": dados["abilities"][0]["ability"]["name"],
                "url": dados["abilities"][0]["ability"]["url"],
                "is_hidden": dados["abilities"][0]["is_hidden"],
                "slot": dados["abilities"][0]["slot"]
            }
            return jsonReturn    