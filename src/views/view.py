from colorama import init, Fore

init()

class GameView:

    # Error dialog.

    def request_error(self, pokemon):
        print(
           Fore.RED + f"[REQUEST ERROR]\n"
                      f"Reason for the error: {pokemon}\n"
                       "The provided Pokémon name or ID does not exist."
        )

    # Pokemon comparison dialogues.

    def are_the_same(self, type,object):
        print(Fore.GREEN + f"{type}: {object}")


    def are_not_the_same(self, type ,object):
        print(Fore.RED + f"{type}: {object}")


    def diference(self, type,object,bigger):
        if bigger:
            print(Fore.YELLOW + f"{type}: {object} ↓")
        else:
            print(Fore.YELLOW + f"{type}: {object} ↑")


    def win(self):
        print(Fore.GREEN + "! Got it right !")


    # User interaction dialogue.

    def ask_for_pokemon(self):
        name_or_id = input(Fore.BLACK + "Who's That Pokémon?: ")
        return name_or_id
    
    # Game information.

    def attempt(self, attempt):
        print(Fore.WHITE + f"attempt: {attempt}")