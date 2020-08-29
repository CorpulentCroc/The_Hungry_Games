class Player:
    def __init__(self, name='', species='', gender='', backstory='', weight=0, inflation=0, berryification=0, status=[], armor=0, inventory=[]):
        self.name = name
        self.species = species
        self.gender = gender
        self.backstory = backstory
        self.weight = weight
        self.inflation = inflation
        self.berryification = berryification
        self.status = status
        self.armor = armor
        self.inventory = inventory
        
    def print_inventory(self):
        for i in range(len(self.inventory)):
                print(f'{i+1}: {self.inventory[i].name}')
                
    def use(self):
        self.print_inventory()
        while True:
            try:
                index = int(input('Enter the number of the item you want to select, or -1 to exit: ')) - 1
                assert index in range(-1, self.inventory.length)
                if index == -1:
                    return "Use cancelled"
            except:
                print("Choose a valid item number or -1")
            break
        item = self.inventory[index]
        type_of = type(item)
        if type_of == "Armor":
            self.use_armor(item)
        elif type_of == "Health_Item":
            self.use_health_item(item)
        else:
            return "Not yet implemented"
        
    def use_armor(self, item):
        self.armor = item.armor_tier.value
        self.inventory.remove(item)
        return self.armor
    
    def use_health_item(self, item):
        if item.health == "BERRY_CURE":
            if "Temp_Berry" in self.status:
                self.status.remove("Temp_Berry")
            elif "Perma_Berry" in self.status:
                self.status.remove("Perma_Berry")
            else:
                return "You appear to already be fine"
            self.inventory.remove(item)
            return "You've been cured from berry status"
        if self.weight == 0 and self.inflation == 0 and self.berryification == 0:
            return "You seem to be fine at the moment"
        self.weight -= item.health
        self.inflation -= item.health
        self.berryification -= item.health
        self.uhi_helper()
        self.inventory.remove(item)
        return "Health restored"
        
    def uhi_helper(self):
        if self.weight < 0:
            self.weight = 0
        if self.inflation < 0:
            self.inflation = 0
        if self.berryification < 0:
            self.berryification = 0

crominulus = Player('Crominulus', 'Crocodile', 'Male')
vyacheslav = Player('Vyacheslav', 'Eastern Dragon', 'Male')
tricia = Player('Tricia', 'Moth', 'Female')
koko = Player('Koko', 'Lucario', 'Male')
liz = Player('Liz', 'Salazzle', 'Female')
brush = Player('Brush', 'Red Panda', 'Male')
midnight = Player('Midnight', 'Cabbit', 'Male')
ray = Player('Ray', 'Fennec Fox', 'Female')
ranz = Player('Ranz', 'Lucario', 'Male')
temp = Player("Temp", "Bubble Dragon", 'Male')
chilly = Player('Chilly', 'Fatass shrew snack', 'Male')