from .Scene import Scene
from .Objects import *
import random
class shop(Scene):
    def __init__(self, surface):
        super().__init__(surface)

        #Background image
        self.bg = Image((0,0),"Scenes/Objects/shopUI.png")
        self.add_object(self.bg)

        #Initialize optional dialogue
        #self.dialogue = Text((350,400), "", font_size=20)
        #self.add_object(self.dialogue)


    def chat(self): 
        #dialogue text options
        dialogue1 = ("Shopkeeper: \"Getting harder to restock.\"")
        dialogue2 = ("Villager: \"Damn I can't afford this!\"")
        dialogue3 = ("Villager: \"Hmm...no more sugar left.\"")
        dialogue4 = ("Adventurer: \"I suppose this axe'll do.\"")
        dialogue5 = ("Villager: \"I do like a bit of dried meat\"")
        dialogue6 = ("Villager: \"Not really a lot here is there?\"")
        dialogue7 = ("""Shopkeeper: \"My order is a week late ugh.
I bet those damn goblins must have got it!\"""")
        


        #return all dialogue options as a list 
        dialogue_options = [dialogue1,dialogue2,dialogue3,dialogue4,dialogue5,dialogue6,dialogue7]
        #self.dialogue.set_text(random.choice(dialogue_options))
        
        self.dialogue = random.choice(dialogue_options)
        
        self.dialogue= self.dialogue.split("\n")
        line_gap = 20
        y = 395
        for line in self.dialogue:
            self.add_object(Text((165,y), line, font_size=20, align="left"))
            y += line_gap

    def reset_text(self):
        self.add_object(Rectangle(pos = (165,385), size = (360,95), colour =(0,0,0)))

    def press(self, key):
        if key == pygame.K_1:
            pass #buy
        if key == pygame.K_2:
            pass #sell
        if key == pygame.K_3:
            self.reset_text()
            self.chat()
        if key == pygame.K_4:
            self.reset_text()
            self.change_scene("caerham")