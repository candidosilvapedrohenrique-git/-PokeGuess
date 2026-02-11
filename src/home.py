import requests
import random
from colorama import init, Fore, Style

init()

# Loop control
hit = False
attempt = 0

# Choose a random Pokémon and request it.
randomPokemon = random.randint(1,151) # There are currently 1025 Pokémon, but I only listed the first 151 because they are the most well-known.
randomUrl = f"https://pokeapi.co/api/v2/pokemon/{randomPokemon}"
randomResponse = requests.get(randomUrl)
randomData = randomResponse.json()
randomName = randomData["name"]
randomHeight = randomData["height"]
randomWeight = randomData["weight"]


while hit != True:
    # Makes the request for the desired Pokémon.
    pokemon = input("Digite o número ou o nome do seu pokemon: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    response = requests.get(url)
    

    # Check if the Pokémon exists.
    if response.status_code != 200:
        print(Fore.RED + "Esse pokemon não existe")
        exit()


    # Convert the files and print them.
    data = response.json()

    name = data["name"]
    height = data["height"]
    weight = data["weight"]


    # Simple if and else statements that control how the game works.
    if randomName != name:
        print(Fore.RED + f"nome: {name}")

    else:
        print(Fore.GREEN + "! Got it right !")
        break

    
    
    if height == randomHeight:
        print(Fore.GREEN + f"Height: {height}cm")

    elif height > randomHeight:
        print(Fore.YELLOW + f"Height: {height}cm ↓")

    elif height < randomHeight:
        print(Fore.YELLOW + f"Height: {height}cm ↑")



    if weight == randomWeight:
        print(Fore.GREEN + f"Weight: {weight}")

    elif weight > randomWeight:
        print(Fore.YELLOW + f"Weight: {weight} ↓")
        
    elif weight < randomWeight:
        print(Fore.YELLOW + f"Weight: {weight} ↑")

    
    attempt += 1
    print(Fore.WHITE + f"attempt: {attempt}")