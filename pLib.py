#player class

class Player:
    def __init__(self, name="", atk = 5, health = 100):
        self.name = name
        self.atk = atk
        self.health = health
        
    def setname(self, name):
        self.name = name
    
    def setatk(self, atk):
        self.atk = atk
        
    def sethealth(self, health):
        self.health = health

    def getatk(self): 
        return self.atk
