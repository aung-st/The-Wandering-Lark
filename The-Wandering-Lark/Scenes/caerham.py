from .Scene import Scene
from .Objects import *

import random


class caerham(Scene):
    
    def __init__(self,
                 surface):
        
        super().__init__(surface)

        # Background image
        self.bg = Image((0,0), "Scenes/Images/villageUI.png")
        self.add_object(self.bg)

        # Initialize optional dialogue
        # self.dialogue = Text((120,270), "", font_size=20, align = "left")
        
        # self.add_object(self.dialogue)

    def chat(self):
        
        # Dialogue text options
        self.dialogue1 = ("Farmer: \"I farm!\"")
        self.dialogue2 = ("Farmer: \"It's almost harvesting season!\"")
        self.dialogue3 = ("""Farmer: \"Every year our yield just gets worse.
There'll come a day when we are all going to starve.\"""")
        self.dialogue4 = ("""Villager: \"Harvey's a weird lad for sure,
but at least with him around we feel a bit safer.\"""")
        self.dialogue5 = ("""Villager: \"Welcome to Caerham! I'm afraid if it's a 
fortune that you seek, then this is the wrong place for it.\"""")
        self.dialogue6 = ("""Harvey: \"I can just sense those damn goblins...
scuttling around those woods there. But now that you're 
here we can finally show them not to mess with us eh?\"""")
        self.dialogue7 = ("""Villager: \"We may not have much here but every 
last person living here has a roof under their head, 
and food on the table. For how much longer? That, 
I don't want to know or think about.\"""")
        self.dialogue8 = ("""Traveller: \"Nice to see a fellow traveller here!
I'm headed to the Gevelian Capital once I've finished
resting up. I hope your journey won't be perilous, 
although that is a rare thing these days.\"""")

        # Return all dialogue options as a list 
        dialogue_options = [self.dialogue1, self.dialogue2,
                            self.dialogue3, self.dialogue4,
                            self.dialogue5, self.dialogue6,
                            self.dialogue7, self.dialogue8]
        self.dialogue = random.choice(dialogue_options)
        
        self.dialogue = self.dialogue.split("\n")
        line_gap = 20
        y = 255
        for line in self.dialogue:
            self.add_object(Text((115,y), line, font_size = 20, align = "left"))
            y += line_gap
        
    def reset_text(self):
        
        self.add_object(Rectangle(pos = (115,245), size = (445,140), colour =(0,0,0)))

    def press(self,
              key):
        
        if key  == pygame.K_1:
            self.reset_text()
            self.change_scene("inn")
        elif key == pygame.K_2:
            self.reset_text()
            self.change_scene("harveys")
        elif key == pygame.K_3:
            self.reset_text()
            self.change_scene("patrol")
        elif key == pygame.K_4:  
            self.reset_text()
            self.chat()       
