class GameControl:
    def __init__(self,pokemon ,gameservice, getpokemon, view):
        self.pokemon = pokemon
        self.gameservice = gameservice
        self.getpokemon = getpokemon
        self.view = view

            
    def execute(self):
        
    
        while True:

            # This part creates a random Pokémon.
            hidden_id = self.gameservice.radom_pokemonIp()
            
            data = self.getpokemon(hidden_id)
            name = data["name"]
            height = data["height"]
            weight = data["weight"]

            hidden_pokemon = self.pokemon(name, height, weight)
            attempt = 0

            while True:
                guessed_pokemon = self.view.ask_for_pokemon()
                
                data = self.getpokemon(guessed_pokemon)
                if data == None:
                    self.view.request_error(guessed_pokemon)
                    break

                name = data["name"]
                height = data["height"]
                weight = data["weight"]

                guessed_pokemon = self.pokemon(name, height, weight)


                right_pokemon = self.gameservice.is_current_guess(hidden_pokemon.name ,guessed_pokemon.name)

                if right_pokemon:
                    self.view.win()
                    break

                else:
                    self.view.are_not_the_same("name" , guessed_pokemon.name)

                        # Height comparisons. 
                    same = self.gameservice.are_the_same(guessed_pokemon.height, hidden_pokemon.height) 

                    if same:
                        self.view.are_the_same("Height", guessed_pokemon.height)

                    else:
                        bigger = self.gameservice.comparasion(guessed_pokemon.height, hidden_pokemon.height)

                        self.view.diference("Height", guessed_pokemon.height, bigger)
                        

                        # Weight comparisons. 
                    same = self.gameservice.are_the_same(guessed_pokemon.weight, hidden_pokemon.weight) 

                    if same:
                        self.view.are_the_same("Weight", guessed_pokemon.weight)

                    else:
                        bigger = self.gameservice.comparasion(guessed_pokemon.weight, hidden_pokemon.weight)

                        self.view.diference("Weight", guessed_pokemon.weight, bigger)

                    

                    # Display of comparison results.
                    

                    attempt +=1
                    self.view.attempt(attempt)
                    