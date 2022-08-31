from .Enemy import Enemy

class Orc(Enemy):
    
    def __init__(self):
        
        super().__init__("Orc", (300,750), (3,5), (1,5), (11,20))
        
        self.level = 3
