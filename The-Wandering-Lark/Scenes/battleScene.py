from EnemyManager import EnemyManager

from .Objects import *
from .Scene import Scene

import random


class battleScene(Scene):
    
    def __init__(self,
                 surface,
                 total_enemies,
                 player,
                 next_scene = "error"):

        super().__init__(surface)
        
        # Initialize battle entities
        self.player = player
        self.enemy = self.generate_enemy()

        # Determine how many enemies to fight in an instance
        self.total_enemies = total_enemies
        self.enemies_killed = 0

        # Where to go after fight has finished
        self.next_scene = next_scene

        # Background image
        self.bg = Image((0,0), "Scenes/Images/battleUI.png")
        self.add_object(self.bg)

        # BattleUI Text
        self.playerStats()
        self.enemyStats()
        self.info_messages()

    def playerStats(self):
        
        # Player stats
        self.player_level = Text((5,15), "", font_size = 20, align = "left")
        self.player_hp = Text((5,35), "", font_size = 20, align = "left")
        self.player_xp = Text((5,75), "", font_size = 20, align = "left")
        self.active = False # Defense Buff

        self.add_object(self.player_level)
        self.add_object(Text((5,55), self.player.name, font_size = 20, align = "left")) # name
        self.add_object(self.player_hp)
        self.add_object(self.player_xp)

    def enemyStats(self):
        
        # Enemy stats
        self.enemy_level = Text((545,15), "", font_size = 20, align = "left")
        self.enemy_hp = Text((545,55), "", font_size = 20, align = "left")
        self.enemy_name = Text((545,35), "", font_size = 20, align = "left")

        # Enemy Text (top RHS)
        self.add_object(self.enemy_level)
        self.add_object(self.enemy_name)
        self.add_object(self.enemy_hp)

    def battleActions(self):
        
        # Actions menu (Bottom)
        self.add_object(Text((365,440), "Options", font_size = 25))
        self.add_object(Text((360,480), "1: Attack", font_size = 30))
        self.add_object(Text((360,510), "2: Defend", font_size = 30))
        self.add_object(Text((360,540), "3: Run", font_size = 30))

    """
    This method will render text objects
    And then have set_text() methods
    called whenever text is to be replaced
    without causing any overlapping on render
    """
    def info_messages(self):
        
        # Set text
        self.player_msg = Text((360,160), "", 20)
        self.enemy_msg =  Text((360,190), "", 20)
        self.inventory_prompt = Text((190,390), "", 20, align = "left")
        
        # Render text to screen
        self.add_object(self.player_msg)
        self.add_object(self.enemy_msg)
        self.add_object(self.inventory_prompt)

    def per_frame(self):
        
        # Called every frame by scene.update()
        self.player_level.set_text(f"Level: {self.player.level}")
        self.player_hp.set_text(f"HP: {self.player.hp}/{self.player.max_hp}")
        self.player_xp.set_text(f"XP: {self.player.xp}/{self.player.xp_cap}")

        self.enemy_level.set_text(f"Level: {self.enemy.level}")
        self.enemy_hp.set_text(f"HP: {self.enemy.hp}/{self.enemy.max_hp}")
        self.enemy_name.set_text(self.enemy.name)

    def attack(self):
        
        # Enemy and player attacks each other and takes damage
        player = self.player.attack(self.enemy)

        # Update attack text after attacking
        if self.enemy.is_dead():
            self.enemies_killed += 1
            if self.enemies_killed == self.total_enemies:
                self.player_msg.set_text("You have killed all enemies!")
                self.enemy_msg.set_text("Press Enter to continue.")
            else:
                # XP drop related
                xp_drop = self.enemy.drop_xp()
                self.player.xp += xp_drop

                # Currency drop related
                gevel_drop = self.enemy.drop_gevels()
                self.player.gevels += gevel_drop

                # Check for level up
                if self.player.xp_cap <= self.player.xp:
                    self.player.level += 1
                    self.player.xp_cap = 5 + (self.player.level * 5)
                    self.player.max_hp += random.randint(20, 50)
                    self.player.hp = self.player.max_hp
                    self.player.xp = 0
                    self.enemy = self.generate_enemy()
                    self.player_msg.set_text(f"{self.enemy.name} dead. {xp_drop} xp and {gevel_drop} gevels gained.")
                    self.enemy_msg.set_text(f"Level up! {self.enemy.name} appears!")
                else:
                    self.enemy = self.generate_enemy()
                    self.player_msg.set_text(f"{self.enemy.name} dead. {xp_drop} xp and {gevel_drop} gevels gained!")
                    self.enemy_msg.set_text(f"{self.enemy.name} appears!")
        else:
            enemy = self.enemy.attack(self.player)
            self.player_msg.set_text(f"you deal {player} damage!")
            self.enemy_msg.set_text(f"{self.enemy.name} deals {enemy} damage!")
            self.check_player_dead()



    """
    This method is supposed to reduce how much damage the player takes
    by a fixed percentage for 3 turns
    """
    def defend(self):
        
        self.player.defend()
        enemy = self.enemy.attack(self.player) # Player doesn't attack during this sequence
        self.player_msg.set_text("You Defend! -30% damage for 3 turns!")
        self.enemy_msg.set_text(f"{self.enemy.name} deals {enemy:.0f} damage!")
        self.check_player_dead()

        return self.active

    """
    This method will prompt the player to try to flee from a battle
    if successfull it will transition to a safe scene otherwise
    the player will take double damage from an enemy in that turn.
    """
    def run(self):
        
        chance = random.randint(0, 9)
        success = False
        if chance >= 7: # 30% chance of running
            success = True
            self.player_msg.set_text("")
            self.enemy_msg.set_text("")
            self.enemies_killed = 0 
            self.enemies = self.generate_enemy()
            self.change_scene("prologueEnd")
        else:
            success = False
            enemy = self.enemy.attack(self.player, multiplier = 2)
            self.player_msg.set_text("You try to run but fail!")
            self.enemy_msg.set_text(f"{self.enemy.name} deals {enemy} damage!")
            self.check_player_dead()

    """
    When called, the state of the player is checked, if they are
    dead then we transition to the game over screen otherwise the
    game carries on as usual
    """
    def check_player_dead(self):
        
        if self.player.is_dead():
            self.reset()
            self.change_scene("gameoverScene")
            
    def reset(self):
        
        # Reinitialize entities
        self.enemies_killed = 0
        self.player_msg.set_text("")
        self.enemy_msg.set_text("")

        # Reinitialize default player attributes
        self.player.max_hp = 100
        self.player.atk = 50
        self.player.hp = self.player.max_hp
        self.player.level = 0
        self.player.xp = 0
        self.player.xp_cap = 5

        # Reinitialize enemy entity
        self.enemy = self.generate_enemy()

    def reset_text(self):
        
        self.add_object(Rectangle(pos = (185,230),
                                  size = (345,160),
                                  colour = (255,0,0)))

    def generate_enemy(self):
        
        # Initialize enemy
        self.generator = EnemyManager()
        self.enemies = self.generator.spawn_enemy()
        current_enemy = random.choice(self.enemies)
        
        return current_enemy

    def press(self,
              key):
        
        if self.enemies_killed == self.total_enemies:
            if key == pygame.K_RETURN:
                self.player_msg.set_text("")
                self.enemy_msg.set_text("")
                self.enemies_killed = 0 
                self.enemy = self.generate_enemy()
                self.change_scene(self.next_scene)
        else: # Don't allow attack or defend after final enemy is dead
            if key == pygame.K_a:
                self.attack()
            elif key == pygame.K_d:
                self.defend()
            elif key == pygame.K_r:
                self.run()

