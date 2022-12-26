import requests
from flask import url_for

class PokemonF(): 
    def getPokemon(name):
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
                
        error = {
            'image': url_for('static', filename='images/not-found.png'),
            'error': True,
            'msg': 'Não identifiquei este pokemon'
        }

        return error
    
    def getAllPokemon():
        result = requests.get('https://pokeapi.co/api/v2/pokemon/?&limit=3')
        dados = result.json()
        listarPokemon = dados["results"]

        allPokemon = []

        for pokemon in listarPokemon:
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
                # "ability": ability,
                # "types": type,
                # "moves":moves
            }
            allPokemon.append(jsonReturn)

        return allPokemon
