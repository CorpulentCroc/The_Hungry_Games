"""
    STATUS: INCOMPLETE
    
    TO ADD/CHANGE: PRACTICALLY THE ENTIRE EVENT CLASS
"""

class Event:
    def __init__(self, name='', location='universal', description='', funct = None):
        self.name = name
        self.location = location
        self.description = description
        self.funct = funct
        
watching_two_players_battle = Event('Coming across two players battling', 'universal', 'You see two players battling each other and can either fight the winner or leave')
battle = Event('Battle', 'universal', 'You are confronted by a player a battle ensues')
back_turned = Event('Coming across a player whose back is turned', 'universal', 'You come across a player unaware of your presence, and can either sneak attack them or leave')
def find_random_item_helper(player, map_biome):
    item_found = map_biome.get_loot()
    while True:
        try:
            choice = int(input(f"You found {item_found}! To pick it up, press 1. To leave, press 2: "))
            if choice == 1:
                player.inventory.append(item_found)
                return "You successfully picked up the item"
            elif choice == 2:
                return "You left the item"
            print("Invalid input")
        except:
            print("Invalid input")
find_random_item = Event("Find random item", 'universal', 'You found a random item! Want to pick it up?', find_random_item_helper)