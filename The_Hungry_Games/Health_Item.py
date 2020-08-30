"""
    STATUS: INCOMPLETE
    
    TO ADD/CHANGE: ADD use()
"""

class Health_Item:
    def __init__(self, name='', health=25):
        self.name = name
        self.health = health
        self._type = 'Health_Item'
        
small = Health_Item('Small Health Kit')
medium = Health_Item('Medium Health Kit', 50)
large = Health_Item('Large Health Kit', 100)
berry_cure = Health_Item('Berry Cure', "BERRY_CURE")
