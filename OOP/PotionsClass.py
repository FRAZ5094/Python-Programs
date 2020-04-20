class Player():
    def __init__(self,Name):
        self.Name=Name
        self.inventory=[]
        self.Health=100
        self.MovementSpeed=10
        self.Invisable=False

    def showStats(self):
        print("Health={}".format(self.Health))
        print("MoveSpeed={}".format(self.MovementSpeed))
        print("Invisable={}".format(self.Invisable))
    
    def drinkPotion(self,Potion):
        if Potion in self.inventory:
            print("You drank a {}".format(Potion.Name))
            Potion.potionEffect(self)
        else:
            print("{} does not have this potion".format(self.Name))

    def addInventory(self,item):
        self.inventory.append(item)

    def showInventory(self):
        for item in self.inventory:
            print("[{}]".format(item))

class Potion():
    def __init__(self,Price):
        self.Price=Price


    
class healthPotion(Potion):
    def __init__(self,Price,healing):
        super().__init__(Price)
        self.healing=healing
        self.Name="Healing Potion"

    def potionEffect(self,Player):
        Player.Health+=self.healing
        print("Health potion healed you by {} health".format(self.healing))
        print("{} now has {} health".format(Player.Name,Player.Health))

    def __repr__(self):
        return "Health Potion,Healing={}".format(self.healing)

class invisPotion(Potion):
    def __init__(self,Price,Duration):
        super().__init__(Price)
        self.Duration=5
        self.Name="Invisablity Potion"
    
    def potionEffect(self,Player):
        if Player.Invisable:
            print("{} is already invisable".format(Player.Name))
        else:
            Player.Invisable=True
            print("{} is now invisable for {} seconds".format(Player.Name,self.Duration))

    def __repr__(self):
        return "Invisbiliy Potion,Duration={} seconds".format(self.Duration)


Fraser=Player("Fraser")
Fraser.addInventory(healthPotion(1000,10))
Fraser.addInventory(invisPotion(1000,5))
Fraser.showInventory()






