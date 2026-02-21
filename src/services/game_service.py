import random

class GameService:

    @staticmethod
    def radom_pokemonIp():
        return random.randint(1,151) # There are currently 1025 Pokémon, but I only listed the first 151 because they are the most well-known.
    
    @staticmethod
    def comparasion(bigger, minor):
        return bigger > minor
        
    @staticmethod
    def are_the_same(object1, object2):
        return object1 == object2
            
        
            


    @staticmethod
    def is_current_guess(hide_name,guess_name):
        return hide_name == guess_name

    