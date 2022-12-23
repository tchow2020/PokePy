from flask_restful import Resource
import requests

class Pokemon(Resource):
    class GetPokemon(Resource):
        def get(self, name):
            name = name.lower()
            result = requests.get('https://pokeapi.co/api/v2/pokemon/?&limit=1154')
            dados = result.json()
            listarPokemon = dados["results"]
            for pokemon in listarPokemon:
                if pokemon["name"] == name:
                    urlPokemon = pokemon["url"]
                    result = requests.get(urlPokemon)
                    dados = result.json()
                   
                    ability = []
                    for i in dados["abilities"]:
                        ability.append(i["ability"]["name"])

                    type = []
                    for i in dados["types"]:
                        type.append(i["type"]["name"])

                    moves = []
                    for i in dados["moves"]:
                       moves.append(i["move"]["name"])

                    jsonReturn = {
                        "image": dados["sprites"]["front_default"],
                        "nome": dados["forms"][0]["name"],
                        "ability": ability,
                        "types": type,
                        "moves":moves
                    }

                    return jsonReturn
                  
            return {
                'error': True,
                'msg': 'Não identifiquei este pokemon'
            }
        
    class Homologação(Resource):
            def get(self):
                result = requests.get('https://pokeapi.co/api/v2/pokemon/1/')
                dados = result.json()

                moves = []
                for i in dados["moves"]:
                    moves.append(i["move"]["name"])

                jsonReturn = {
                    "move": moves
                }
                return jsonReturn