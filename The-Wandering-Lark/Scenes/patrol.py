from .battleScene import battleScene
from .Objects import *

import random


class patrol(battleScene):

    def __init__(self, 
                 surface,
                 total_enemies,
                 player):

        super().__init__(surface, total_enemies, player, "caerham")

    def run(self):

        chance = random.randint(0, 9)
        success = False
        
        if chance >= 7: #30% chance of running
            success = True
            self.player_msg.set_text("")
            self.enemy_msg.set_text("")
            self.enemies_killed = 0 
            self.enemies = self.generator.spawn_enemy()
            self.change_scene("caerham")
        else:
            success = False
            enemy = self.enemy.attack(self.player,multiplier = 2)
            self.player_msg.set_text("You try to run but fail!")
            self.enemy_msg.set_text(f"{self.enemy.name} deals {enemy} damage!")
            self.check_player_dead()
