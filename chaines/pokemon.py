import requests

def interroger_PokeAPI(identifiant):
    reponse = requests.get(f"https://pokeapi.co/api/v2/pokemon/{identifiant}").json()
    nom = reponse['name'].capitalize()
    taille = round(reponse['height']*10)
    poids = round(reponse['weight']/10)
    xp = reponse['base_experience']
    sprite = reponse['sprites']['front_default']
    return {'nom' : nom, 'taille' : taille, 'poids' : poids, 'xp' : xp, 'sprite' : sprite}

def extraire_donnee(pokemon, donnee):
    if type(pokemon) != dict or type(donnee) != str:
        raise TypeError('le premier argument doit être un "pokemon", le second une chaîne')
    if donnee not in ['nom', 'taille', 'poids', 'xp', 'sprite']:
        raise ValueError('le second argument doit être "nom", "taille", "poids", "xp" ou "sprite"')
    return pokemon[donnee]