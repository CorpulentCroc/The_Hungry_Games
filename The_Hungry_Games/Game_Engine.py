"""
    STATUS: INCOMPLETE
    
    TO ADD/CHANGE: THE REST OF THE GAME ENGINE
"""

import Player
import Biome
import Event

PLAYER_COUNT = 24
PLAYER_LIST = [Player.Player() for i in range(24)]
GAME_STATE = "Normal" 
MAP = Biome.forest

print(Event.find_random_item.funct(Player.crominulus, MAP))
Player.crominulus.print_inventory() 