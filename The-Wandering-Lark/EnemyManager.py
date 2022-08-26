import random
from Entities import *




class EnemyManager():
    def __init__(self):
        pass   

    def spawn_enemy(self):
        goblin = Goblin()
        orc = Orc()
        enemies = []
        enemies.append(goblin)
        enemies.append(orc)
        return enemies

