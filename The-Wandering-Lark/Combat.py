from Entities import Player
from EnemyManager import EnemyManager
import random

# TODO: MAKE SCENE

class Combat():
    def __init__(self,player): 
        #initialize player and enemies
        self.generator = EnemyManager()
        self.enemies = self.generator.spawn_enemy()
        self.player = player
        self.current_enemy = random.choice(self.enemies)
"""
    def attack(self):
        #Player's turn
        attack_enemy = self.player.attack(self.enemy)
        attack_enemy
        self.enemy_damage_taken = attack_enemy.damage

        #Enemy's turn 
        attack_player = self.enemy.attack(self.player)
        attack_player 
        self.player_damage_taken = attack_player.damage"""

