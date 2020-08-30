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
def battle_helper(p, rng_func, l):
    opponent = rng_func(l)
    print(f'A battle with {opponent.name} has begun!')
    if not p.has_weapon() and not opponent.has_weapon():
        print('Neither of you have weapons, so the battle ended in a draw.')
    elif not p.has_weapon():
        print('You don\'t have a weapon, and thus lost.')
        return 'loss'
    elif not opponent.has_weapon():
        print('Your opponent doesn\'t have a weapon, and thus lost.')
        return opponent
    while True:
        try:
            weapon_num_choice = int(input(f'Choose a valid weapon from your inventory to fight with: {p.print_weapons()}: '))
            assert p.inventory[weapon_num_choice-1]._type == 'Weapon'
            weapon_choice = p.inventory[weapon_num_choice-1]
        except:
            print('Enter your input as a valid integer')
        break
    #To be implemented
        
battle = Event('Battle', 'universal', 'You are confronted by a player a battle ensues')
back_turned = Event('Coming across a player whose back is turned', 'universal', 'You come across a player unaware of your presence, and can either sneak attack them or leave')
final_battle = Event('You and only one other player remain', 'universal', 'You are forced to the middle, you spot the other player, this is the battle for victory!')
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
#Not yet working \/
def random_player_eliminated_helper():
    pass
random_player_eliminated = Event('Random player eliminated', 'universal', 'A random player was eliminated.', random_player_eliminated_helper)
