"""Change the get_loot() function"""

import Weapon
class Biome:
    def __init__(self, name='', description='', loot_pool=[], event_list=[]):
        self.name = name
        self.description = description
        self.loot_pool = loot_pool
        self.event_list = event_list
    def get_loot(self):
        """Change this ASAP"""
        return self.loot_pool[0]

forest = Biome("Forest", loot_pool=[Weapon.fat_pistol])
desert = Biome("Desert")
urban = Biome("Urban")
beach = Biome("Beach")
tundra = Biome("Tundra")