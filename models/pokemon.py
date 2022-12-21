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
                    jsonReturn = {
                        "nome": dados["forms"][0]["name"],
                        "ability-1": dados["abilities"][0]["ability"]["name"],
                        "ability-2": dados["abilities"][1]["ability"]["name"],
                        "image": dados["sprites"]["front_default"]
                    }
                    return jsonReturn
            
            return {
                'error': True,
                'msg': 'Não identifiquei este pokemon'
            }
        
    # class Image(Resource):
    #     def get(self, url):
    #         result = requests.get(url)
    #         dados = result.json()
    #         jsonReturn = {
    #             "nome": dados["forms"][0]["name"],
    #             "ability-1": dados["abilities"][0]["ability"]["name"],
    #             "ability-2": dados["abilities"][1]["ability"]["name"]
    #         }
    #         return jsonReturn