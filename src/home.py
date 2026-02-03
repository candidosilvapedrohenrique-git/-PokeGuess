import requests

pokemon = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

response = requests.get(url)

if response.status_code != 200:
    print("Pokémon não encontrado")
    exit()

data = response.json()

name = data["name"]
height = data["height"]
types = [t["type"]["name"] for t in data["types"]]
image = data["sprites"]["front_default"]

print(f"Nome: {name}")
print(f"Altura: {height}")
print(f"Tipos: {', '.join(types)}")
print(f"Imagem: {image}")
