from controllers.game_control import GameControl
from models.pokemon import Pokemon
from services.game_service import GameService
from infra.pokemon_api_client import get_pokemon
from views.view import GameView

view = GameView()
service = GameService()

game = GameControl(
    Pokemon, 
    service, 
    get_pokemon, 
    view
    )

game.execute()

