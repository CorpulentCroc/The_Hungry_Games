import enum

class Damage_Type(enum.Enum):
    FAT="fat"
    INFLATION="inflation"
    BERRY="berry"

class Weapon_Type(enum.Enum):
    BOW="bow"
    LMG="lmg"
    ASSAULT_RIFLE="assault_rifle"
    SMG="smg"
    PISTOL="pistol"
    SNIPER_RIFLE="sniper_rifle"
    SEMIAUTO_RIFLE="semiauto_rifle"
    SPECIAL_WEAPON="special_weapon"
    
weapon_type_value_dict = {"bow": (70, 50, 30, 70), "lmg": (50, 30, 15, 80), "assault_rifle": (35, 20, 10, 85), "smg": (25, 15, 5, 90),
                          "pistol": (20, 10, 5, 95), "sniper_rifle": (90, 65, 40, 90), "semiauto_rifle": (40, 25, 15, 80), "special_weapon": (80, 80, 80, 70)}

class Weapon:
    def __init__(self, name='', damage_type=Damage_Type.FAT, weapon_type=None):
        self.name = name
        self.damage_type = damage_type
        self.weapon_type = weapon_type
        self.h_dmg, self.b_dmg, self.l_dmg, self.accuracy = weapon_type_value_dict[self.weapon_type.value]
    def __str__(self):
        return self.name
        
fat_bow = Weapon("Fat Bow", Damage_Type.FAT, Weapon_Type.BOW)
fat_lmg = Weapon("Fat LMG", Damage_Type.FAT, Weapon_Type.LMG)
fat_assault_rifle = Weapon("Fat Assault Rifle", Damage_Type.FAT, Weapon_Type.ASSAULT_RIFLE)
fat_submachine_gun = Weapon("Fat Submachine Gun", Damage_Type.FAT, Weapon_Type.SMG)
fat_pistol = Weapon("Fat Pistol", Damage_Type.FAT, Weapon_Type.PISTOL)
fat_sniper_rifle = Weapon("Fat Sniper Rifle", Damage_Type.FAT, Weapon_Type.SNIPER_RIFLE)
fat_semiauto_rifle = Weapon("Fat Semi-Auto Rifle", Damage_Type.FAT, Weapon_Type.SEMIAUTO_RIFLE)
gatling_cake_gun = Weapon("Gatling Cake Gun", Damage_Type.FAT, Weapon_Type.SPECIAL_WEAPON
"""
Unused for now \/

inflation_bow = Weapon("Inflation Bow", Damage_Type.INFLATION, 50, Weapon_Type.BOW)
inflation_lmg = Weapon("Inflation LMG", Damage_Type.INFLATION, 30, Weapon_Type.LMG)
inflation_assault_rifle = Weapon("Inflation Assault Rifle", Damage_Type.INFLATION, 20, Weapon_Type.ASSAULT_RIFLE)
inflation_submachine_gun = Weapon("Inflation Submachine Gun", Damage_Type.INFLATION, 15, Weapon_Type.SMG)
inflation_pistol = Weapon("Inflation Pistol", Damage_Type.INFLATION, 10, Weapon_Type.PISTOL)
inflation_sniper_rifle = Weapon("Inflation Sniper Rifle", Damage_Type.INFLATION, 65, Weapon_Type.SNIPER_RIFLE)
inflation_semiauto_rifle = Weapon("Inflation Semi-Auto Rifle", Damage_Type.INFLATION, 25, Weapon_Type.SEMIAUTO_RIFLE)

#Need to add berry effect

berry_bow = Weapon("Berry Bow", Damage_Type.BERRY, 50, Weapon_Type.BOW)
berry_lmg = Weapon("Berry LMG", Damage_Type.BERRY, 30, Weapon_Type.LMG)
berry_assault_rifle = Weapon("Berry Assault Rifle", Damage_Type.BERRY, 20, Weapon_Type.ASSAULT_RIFLE)
berry_submachine_gun = Weapon("Berry Submachine Gun", Damage_Type.BERRY, 15, Weapon_Type.SMG)
berry_pistol = Weapon("Berry Pistol", Damage_Type.BERRY, 10, Weapon_Type.PISTOL)
berry_sniper_rifle = Weapon("Berry Sniper Rifle", Damage_Type.BERRY, 65, Weapon_Type.SNIPER_RIFLE)
berry_semiauto_rifle = Weapon("Berry Semi-Auto Rifle", Damage_Type.BERRY, 25, Weapon_Type.SEMIAUTO_RIFLE)
berry_beam = Weapon("Berry Beam", Damage_Type.BERRY, 80, Weapon_Type.BEAM)
"""
