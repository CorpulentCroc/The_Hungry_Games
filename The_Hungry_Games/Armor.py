"""
    STATUS: COMPLETE
"""

import enum

class Armor_Tiers(enum.IntEnum):
    TIER_1 = 50
    TIER_2 = 100
    TIER_3 = 150
    TIER_4 = 200
    
class Armor:
    def __init__(self, name='', armor_tier=Armor_Tiers.TIER_1):
        self.name = name
        self.armor_tier = armor_tier
        self._type = 'Armor'
        
t1 = Armor("Tier 1 Armor")
t2 = Armor("Tier 2 Armor", Armor_Tiers.TIER_2)
t3 = Armor("Tier 3 Armor", Armor_Tiers.TIER_3)
t4 = Armor("Tier 4 Armor", Armor_Tiers.TIER_4)
