from .Entity import Entity


class Player(Entity):
    
    def __init__(self,
                 name): # Base stats
        
        super().__init__(name)
        
        self.max_hp = 100
        self.atk = 50
        self.name = name
        self.hp = self.max_hp
        self.level = 0
        self.xp = 0
        self.xp_cap = 5 + (self.level * 5)
        self.gevels = 0

