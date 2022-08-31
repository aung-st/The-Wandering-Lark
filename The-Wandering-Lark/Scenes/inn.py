from .Scene import Scene
from .Objects import *
import random
class inn(Scene):
    def __init__(self, surface,player):
        super().__init__(surface)

        #intialize player
        self.player = player

        #Background image
        self.bg = Image((0,0),"Scenes/Objects/innUI.png")
        self.add_object(self.bg)

        #Initialize optional dialogue
        #self.dialogue = Text((135,285), "", font_size=20, align = "left")

        #self.add_object(self.dialogue)
    def buy(self):
        pass

    def rest(self):
        self.reset_text()
        if self.player.hp != self.player.max_hp:
            if self.player.gevels < 10:
                    self.reset_text()
                    self.add_object(Text((130,305),"You can't afford that!", font_size=20, align="left"))
            else:
                self.reset_text()
                self.add_object(Text((130,305),"You rest for a night. Regain all HP!", font_size=20, align="left"))
                self.player.hp = self.player.max_hp
            
        else:
            self.add_object(Text((130,285), "You don't need any rest yet.", font_size=20, align="left"))





    def chat(self): 
        #dialogue text options
        dialogue1 = ("Barfly: \"Good god there's two of you!\"")
        dialogue2 = ("Villager: \"Nothing like an ale to warm my belly!\"")
        dialogue3 = ("Villager: \"Cheapest place to keep yourself warm this is.\"")
        dialogue4 = ("Villager: \"Nothing much in Caerham you know.\"")
        dialogue5 = ("Barfly: \"How do you ~hicc do?\"")
        dialogue6 = ("Musician: \"Got any requests?\"")
        dialogue7 = ("Musician: \"A tip is always appreciated.\"")
        dialogue8 = ("""Innkeeper: \"Only 10 gevels to a night stay in our rooms! 
An absolute steal!\"""")
        dialogue9 = ("Innkeeper: \"Oh dear, time to clean sick off that table.\"")
        dialogue10 = ("Innkeeper: \"Always nice to see a new face.\"")
        dialogue11 = ("""Villager: \"Didn't feel like cooking at all today 
so here I am.\"""")
        dialogue12 = ("""Farmer: \"I come here whenever I can afford to after a 
long day toiling in the fields. Not that theres is a whole 
lot to toil these days.\"""")

        #return all dialogue options as a list 
        dialogue_options = [dialogue1,dialogue2,dialogue3,dialogue4,dialogue5,dialogue6,
                            dialogue7,dialogue8,dialogue9,dialogue10,dialogue11,dialogue12]
        
        #self.dialogue.set_text(random.choice(dialogue_options))
        self.dialogue = random.choice(dialogue_options)
        
        self.dialogue= self.dialogue.split("\n")
        line_gap = 20
        y = 285
        for line in self.dialogue:
            self.add_object(Text((130,y), line, font_size=20, align="left"))
            y += line_gap
        
        
    def reset_text(self):
        self.add_object(Rectangle(pos = (130,275), size = (445,135), colour =(0,0,0)))



    def press(self, key):
        if key == pygame.K_1:
            self.reset_text()
            self.chat()
        elif key == pygame.K_2:
            self.rest()
        elif key == pygame.K_3:
            self.reset_text()
            self.change_scene("caerham")
       