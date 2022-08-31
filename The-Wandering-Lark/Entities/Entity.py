import random
from math import ceil

class Entity():
    
    def __init__(self,
                 name): # Base stats
        
        self.name = name
        self.max_hp = 1
        self.hp = 1
        self.atk = 1
        self.gevels = 0
        self.damage_multiplier = 1 # Damage dealt to this entity
        self.defending = 0 # Defending for how many hits

    def take_damage(self,
                    amount):
        
        damage = ceil(self.damage_multiplier * amount)
        self.hp = max(self.hp - damage, 0)
        
        if not self.defending:
            self.damage_multiplier = 1
        else:
            self.defending -= 1

        return damage

    def heal(self,
             amount):
        
        if not self.is_dead():
            self.hp = min(self.hp + amount, self.max_hp)

    def attack(self,
               target,
               multiplier = 1): # Target is another entity
        
        damage = multiplier * random.randint((self.atk * 2), (self.atk * 5)) #An integer between the lower-upper bounds
        damage = ceil(damage) # Round up
        damage = target.take_damage(damage) # Return how much damage target takes
        
        return damage

    def defend(self):
        
        # Duration = 3 hits, defend 30% of damage
        self.damage_multiplier = 0.7
        self.defending = 3

    def is_dead(self):
        
        return self.hp <= 0
