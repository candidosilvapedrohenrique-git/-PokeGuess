import requests
import random
from colorama import init, Fore, Style

init()

hit = False
attempt = 0

while hit != True:
    # Makes the request for the desired Pokémon.
    pokemon = input("Digite o número ou o nome do seu pokemon: ")
    randomPokemon = random.randint(1,151) # Existem atualmente 1025 Pokemons
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    randomUrl = f"https://pokeapi.co/api/v2/pokemon/{randomPokemon}"

    response = requests.get(url)
    randomResponse = requests.get(randomUrl)

    # Check if the Pokémon exists.
    if response.status_code != 200:
        print(Fore.RED + "Esse pokemon não existe")
        exit()


    # Convert the files and print them.
    data = response.json()
    randomData = randomResponse.json()

    name = data["name"]
    height = data["height"]
    weight = data["weight"]

    randomName = randomData["name"]
    randomHeight = randomData["height"]
    randomWeight = randomData["weight"]

    if randomName != name:
        print(Fore.RED + f"nome: {name}")

    else:
        print(Fore.GREEN + f"! Acertou !")
        break

    if height == randomHeight:
        print(Fore.GREEN + f"Altura: {height}")

    elif height > randomHeight:
        print(Fore.YELLOW + f"Altura: {height} ↓")

    elif height < randomHeight:
        print(Fore.YELLOW + f"Altura: {height} ↑")



    if weight == randomWeight:
        print(Fore.GREEN + f"Peso: {weight}")

    elif weight > randomWeight:
        print(Fore.YELLOW + f"Peso: {weight} ↓")
        
    elif weight < randomWeight:
        print(Fore.YELLOW + f"Peso: {weight} ↑")


    attempt += 1
    print(Fore.WHITE + f"attempt: {attempt}")