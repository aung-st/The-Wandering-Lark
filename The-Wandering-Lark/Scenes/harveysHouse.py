from .Scene import Scene
from .Objects import *
import random
class harveysHouse(Scene):
    def __init__(self, surface):
        super().__init__(surface)

        #Background image
        self.bg = Image((0,0),"Scenes/Objects/harveysUI.png")
        self.add_object(self.bg)

    def chat(self): 
        #dialogue text options
        dialogue1 = ("Harvey: Hello.\"\"")
        dialogue2 = ("Harvey: No goblins here I see.\"\"")
        dialogue3 = ("Harvey: I need to get a new pitchfork\"\"")
        dialogue4 = ("Harvey: \"\"")
        dialogue5 = ("Harvey: \"\"")
        dialogue6 = ("Harvey: \"\"")
        dialogue7 = ("""Harvey: \"\"""")
        


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
            self.reset_text()
            self.chat()
        if key == pygame.K_2:
            self.reset_text()
            self.change_scene("caerham")
     