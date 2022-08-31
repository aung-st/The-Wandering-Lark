from Entities.Enemy import Enemy
from Entities.Player import Player
from Entities.Healing_Potion import Healing_Potion
from EnemyManager import EnemyManager
import random

from .Objects import *
from .Scene import Scene
from .Objects import *
#from Combat import Combat
import pygame
class battleScene(Scene):
    def __init__(self, surface, total_enemies,player,next_scene="error"):
        super().__init__(surface)
        
        
        #Initialize battle entities
        self.player = player
        self.enemy = self.generate_enemy()

        #Initialize Inventory
        self.Inventory = player.inventory

        #Determine how many enemies to fight in an instance
        self.total_enemies = total_enemies
        self.enemies_killed = 0

        #Where to go after fight has finished
        self.next_scene = next_scene

        #Background image
        self.bg = Image((0,0),"Scenes/Objects/battleUI.png")
        self.add_object(self.bg)

        #BattleUI Text
        self.playerStats()
        self.enemyStats()
        self.info_messages()
        #self.inventory()


    def playerStats(self):
        #Player stats
        self.player_level = Text((5,15), "", font_size=20,align="left")
        self.player_hp = Text((5,35), "", font_size=20,align="left")
        self.player_xp = Text((5,75), "", font_size=20,align="left")
        self.active = False #Defense Buff

        self.add_object(self.player_level)
        self.add_object(Text((5,55),self.player.name, font_size=20,align="left")) # name
        self.add_object(self.player_hp)
        self.add_object(self.player_xp)


    def enemyStats(self):
        #Enemy stats
        self.enemy_level = Text((545,15), "", font_size=20,align="left")
        self.enemy_hp = Text((545,55), "", font_size=20,align="left")
        self.enemy_name = Text((545,35), "", font_size = 20,align="left")

        #Enemy Text (top RHS)
        self.add_object(self.enemy_level)
        self.add_object(self.enemy_name)
        self.add_object(self.enemy_hp)


    def battleActions(self):
        #Actions menu (Bottom)
        self.add_object(Text((365,440),"Options", font_size=25))
        self.add_object(Text((360,480),"1: Attack", font_size=30))
        self.add_object(Text((360,510),"2: Defend", font_size=30))
        self.add_object(Text((360,540),"3: Inventory", font_size=30))
        self.add_object(Text((360,570),"4: Run", font_size=30))

    

    """
    This method will render text objects
    And then have set_text() methods
    called whenever text is to be replaced
    without causing any overlapping on render
    """
    def info_messages(self):
        #Set text
        self.player_msg = Text((360,160), "",20)
        self.enemy_msg =  Text((360,190), "",20)
        self.inventory_prompt = Text((190,390),"", 20, align= "left")
        #Render text to screen
        self.add_object(self.player_msg)
        self.add_object(self.enemy_msg)
        self.add_object(self.inventory_prompt)

    def per_frame(self):
        # called every frame by scene.update()
        self.player_level.set_text(f"Level: {self.player.level}")
        self.player_hp.set_text(f"HP: {self.player.hp}/{self.player.max_hp}")
        self.player_xp.set_text(f"XP: {self.player.xp}/{self.player.xp_cap}")

        self.enemy_level.set_text(f"Level: {self.enemy.level}")
        self.enemy_hp.set_text(f"HP: {self.enemy.hp}/{self.enemy.max_hp}")
        self.enemy_name.set_text(self.enemy.name)

    def attack(self):
        #enemy and player attacks each other and takes damage
        player = self.player.attack(self.enemy)

        #update attack text after attacking
        if self.enemy.is_dead():
            self.enemies_killed += 1
            if self.enemies_killed == self.total_enemies:
                self.player_msg.set_text(f"You have killed all enemies!")
                self.enemy_msg.set_text(f"Press Enter to continue.")
            else:
                #XP drop related
                xp_drop = self.enemy.drop_xp()
                self.player.xp += xp_drop

                #Currency drop related
                gevel_drop = self.enemy.drop_gevels()
                self.player.gevels += gevel_drop

                #Check for level up
                if self.player.xp_cap <= self.player.xp:
                    self.player.level += 1
                    self.player.xp_cap = 5 + (self.player.level*5)
                    self.player.max_hp += random.randint(20,50)
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
        enemy = self.enemy.attack(self.player) #Player doesn't attack during this sequence
        self.player_msg.set_text(f"You Defend! -30% damage for 3 turns!")
        self.enemy_msg.set_text(f"{self.enemy.name} deals {enemy:.0f} damage!")
        self.check_player_dead()


        return self.active

    #A system will need to be implemented at a future date
    def inventory(self):
        # A list like the following:
        # ["-","-",...]

        self.add_object(Text((360,240), f"Inventory", font_size = 20))

        line_gap = 20
        y = 270
        
        self.Inventory[0] = Healing_Potion()
        self.Inventory[7] = "bills"
        self.Inventory[4] = "bells"
        display_inventory = self.Inventory
        display_inventory[0] = display_inventory[0].name

        for i in range(5):
            self.add_object(Text((260,y), f"{self.Inventory[i]}", font_size=20))
            self.add_object(Text((450,y), f"{self.Inventory[i+1]}", font_size=20,))

            y += line_gap
        
        
    def prompt_use(self):
        self.add_object(Button((400,390),"Y"))
        self.add_object(Button((460,390),"N"))

        
        

    """
    This method will prompt the player to try to flee from a battle
    if successfull it will transition to a safe scene otherwise
    the player will take double damage from an enemy in that turn.
    """
    def run(self):
        chance = random.choice(range(0, 10, 1))
        success = False
        if chance >= 7: #30% chance of running
            success = True
            self.player_msg.set_text("")
            self.enemy_msg.set_text("")
            self.enemies_killed = 0 
            self.enemies = self.generate_enemy()
            self.change_scene("prologueEnd")
        else:
            success = False
            enemy = self.enemy.attack(self.player,multiplier = 2)
            self.player_msg.set_text(f"You try to run but fail!")
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
        #Reinitialize entities
        self.enemies_killed = 0
        self.player_msg.set_text(f"")
        self.enemy_msg.set_text(f"")

        #reinitialize default player attributes
        self.player.max_hp = 100
        self.player.atk = 50
        self.player.hp = self.player.max_hp
        self.player.level = 0
        self.player.xp = 0
        self.player.xp_cap = 5
        self.player.inventory = [None]*10

        #reinitialize enemy entity
        self.enemy = self.generate_enemy()

    


    def reset_text(self):
        self.add_object(Rectangle(pos = (185,230), size = (345,160), colour =(255,0,0)))

    def generate_enemy(self):
        #initialize enemy
        self.generator = EnemyManager()
        self.enemies = self.generator.spawn_enemy()
        current_enemy = random.choice(self.enemies)
        return current_enemy

    def press(self, key):
        if self.enemies_killed == self.total_enemies:
            if key == pygame.K_RETURN:
                self.player_msg.set_text("")
                self.enemy_msg.set_text("")
                self.enemies_killed = 0 
                self.enemy = self.generate_enemy()
                self.change_scene(self.next_scene)
        else: # don't allow attack or defend after final enemy is dead
            if key == pygame.K_a:
                self.attack()
            elif key == pygame.K_d:
                self.defend()
            elif key == pygame.K_r:
                self.run()
            elif key == pygame.K_1:
                if self.Inventory[0] != "-":
                    self.prompt_use()
                    self.inventory_prompt.set_text(f"Use {self.Inventory[0]}?")
            elif key == pygame.K_2:
                if self.Inventory[1] != "-":
                    self.inventory_prompt.set_text(f"Use {self.Inventory[1]}?")
            elif key == pygame.K_3:
                if self.Inventory[2] != "-":
                    self.inventory_prompt.set_text(f"Use {self.Inventory[2]}?")
            elif key == pygame.K_4:
                if self.Inventory[3] != "-":
                    self.inventory_prompt.set_text(f"Use {self.Inventory[3]}?")
            elif key == pygame.K_5:
                if self.Inventory[4] != "-":
                    self.inventory_prompt.set_text(f"Use {self.Inventory[4]}?")
            elif key == pygame.K_6:
                if self.Inventory[5] != "-":
                    self.inventory_prompt.set_text(f"Use {self.Inventory[5]}?")
            elif key == pygame.K_7:
                if self.Inventory[6] != "-":
                    self.inventory_prompt.set_text(f"Use {self.Inventory[6]}?")
            elif key == pygame.K_8:
                if self.Inventory[7] != "-":
                    self.inventory_prompt.set_text(f"Use {self.Inventory[7]}?")
            elif key == pygame.K_9:
                if self.Inventory[8] != "-":
                    self.inventory_prompt.set_text(f"Use {self.Inventory[8]}?")
            elif key == pygame.K_0:
                if self.Inventory[9] != "-":
                    self.inventory_prompt.set_text(f"Use {self.Inventory[9]}?")
          

                
                

