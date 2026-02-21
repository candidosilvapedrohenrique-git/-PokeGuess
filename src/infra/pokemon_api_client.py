import requests

def get_pokemon(id_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{id_name}"
    try:
        response = requests.get(url)
    except requests.RequestException:
        return None
        

    if response.status_code != 200:
        return None
    else:
        return response.json()

