from .Scene import Scene
from .Objects import *

import random


class harveysHouse(Scene):
    
    def __init__(self,
                 surface):
        
        super().__init__(surface)

        # Background image
        self.bg = Image((0,0), "Scenes/Images/harveysUI.png")
        self.add_object(self.bg)

    def chat(self):
        
        # Dialogue text options
        dialogue1 = "Harvey: \"Hello.\""
        dialogue2 = "Harvey: \"No goblins here I see.\""
        dialogue3 = "Harvey: \"I need a new pitchfork.\""
        dialogue4 = """Amy: \"Oh hello there. I'm Harvey's
sister.\""""
        dialogue5 = """Amy: \"I wasn't sure if you were going 
to make it. Those were some terrible 
injuries. You're really lucky to have 
made it out alive from those goblins.\""""
        dialogue6 = """Harvey: \"Oh I forgot to mention
my sister amy! My memory isn't what  
it used to be!\""""
        dialogue7 = """Amy: \"Our parents passed when
we were little. So now it's just me 
and Harvey.\""""
        

        # Return all dialogue options as a list 
        dialogue_options = [dialogue1, dialogue2,
                            dialogue3, dialogue4,
                            dialogue5, dialogue6,
                            dialogue7]
        
        #self.dialogue.set_text(random.choice(dialogue_options))
        
        self.dialogue = random.choice(dialogue_options)
        
        self.dialogue= self.dialogue.split("\n")
        line_gap = 20
        y = 285
        for line in self.dialogue:
            self.add_object(Text((205,y), line, font_size = 20, align = "left"))
            y += line_gap

    def reset_text(self):
        
        self.add_object(Rectangle(pos = (205,270), size = (305,175), colour =(0,0,0)))

    def press(self,
              key):
        
        if key == pygame.K_1:
            self.reset_text()
            self.chat()
        if key == pygame.K_2:
            self.reset_text()
            self.change_scene("caerham")
     
