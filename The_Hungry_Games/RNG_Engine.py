"""
    STATUS: INCOMPLETE
    
    TO ADD/CHANGE: MAP GENERATION, LOOT GENERATION, CRIT RNG, EVENT RNG
"""

import random
import Game_Engine
def choose_player(num=1, pop=False):
    temp_list = Game_Engine.PLAYER_LIST
    temp_count = Game_Engine.PLAYER_COUNT
    result = []
    for _ in range(num):
        player_index = random.randint(1, temp_count)
        player = temp_list[player_index-1]
        if pop:
            temp_list.remove(player)
            temp_count -= 1
        result.append(player)
    return result

def generate_map(custom_seed=None):
    pass