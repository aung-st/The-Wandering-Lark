from .Scene import Scene
from .Objects import *
import random
class caerham(Scene):
    def __init__(self, surface):
        super().__init__(surface)

        #Background image
        self.bg = Image((0,0),"Scenes/Objects/villageUI.png")
        self.add_object(self.bg)

        #Initialize optional dialogue
        #self.dialogue = Text((120,270), "", font_size=20, align = "left")
        

        
        #self.add_object(self.dialogue)

    def chat(self):
        #dialogue text options
        self.dialogue1 = ("Farmer: \"I farm\"")
        self.dialogue2 = ("Villager: \"I village\"")
        self.dialogue3 = ("Villager: \"I'm cold\"")

        #return all dialogue options as a list 
        dialogue_options = [self.dialogue1,self.dialogue2,self.dialogue3]
        self.dialogue = random.choice(dialogue_options)
        
        self.dialogue= self.dialogue.split("\n")
        line_gap = 20
        y = 255
        for line in self.dialogue:
            self.add_object(Text((115,y), line, font_size=20, align="left"))
            y += line_gap
        
    def reset_text(self):
        self.add_object(Rectangle(pos = (115,245), size = (445,140), colour =(0,0,0)))

    def press(self, key):
        if key  == pygame.K_1:
            self.reset_text()
            self.change_scene("inn")
        if key == pygame.K_2:
            self.reset_text()
            self.change_scene("shop")
        if key == pygame.K_3:
            self.reset_text()
            self.change_scene("patrol")
        if key == pygame.K_4:  
            self.reset_text()
            self.chat()       