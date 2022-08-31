from .Entity import Entity

import random


class Enemy(Entity):
    
    def __init__(self,
                 name,
                 hp_range,
                 atk_range,
                 xp_range,
                 gevels_range): # Base stats
        
        super().__init__(name)

        self.hp_range = hp_range
        self.atk_range = atk_range
        self.xp_range = xp_range
        self.gevels_range = gevels_range
        
        self.randomize_init()

    def randomize_init(self):
        
        # Sets health and attack to random values within hp range and atk range
        # Could be modified if you want hp to always be a multiple of something
        self.max_hp = random.randint(*self.hp_range)
        self.hp = self.max_hp
        self.atk = random.randint(*self.atk_range)

    def drop_xp(self):
        
        return random.randint(*self.xp_range)

    def drop_gevels(self):
        
        return random.randint(*self.gevels_range)
        

