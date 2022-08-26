from .Scene import Scene
from .Objects import *

class prologueEnd(Scene):
    def __init__(self, surface):
        super().__init__(surface)
        story = """
        You have now successfully fended yourself from the pack of goblins with your
        life intact. The fatigue punches you again in no time. You carry on making your way 
        through the pitch black of the woods with every inch of willpower left in you. 
        Eventually your body gives up and you find yourself collapsing 
        onto the cold, cracked dirt...

        When you come to, instead of the barely visible foreground,
        you notice a dilapidated village in the distance. 
        Every muscle in you aches as you clumsily drag yourself 
        into the direction of the village. Once every tree is behind you, 
        and you are in full view of the villagers, 
        you are stopped by one very burly man holding a rusty pitchfork.

        "You look like a right mess you do. I'm surprised you made 
        it out of those damned woods. Lucky bastard you are!" He exclaimed. 
        
        You sigh with relief, "Thanks for the warm welcome, though I say that right now
        I feel half dead after the night I had". 
      
        "Only half dead I see, and with all your limbs intact! You still managed to get away 
        from those goblin pricks better than most of us here could anyway!", He replied.
       
        You laugh politely, "You know... I feel rather dizzy right now,
        don't suppose you could let a traveller hunker down for a while?", you ask.

        "Oh that'll probably be that nasty wound on your head", He says.
        
        You notice blood dripping on the floor, "Ah that explains it...", and pass out yet again. 
        The last thing you heard was the man's raucous laughter. 
        """
        story = story.split("\n")
        line_gap = 20
        y = 5

        for line in story:
            self.add_object(Text((0,y), line, font_size=20, align = "left"))
            y += line_gap
        


    def press(self, key):
        if key == pygame.K_RETURN:
            self.change_scene("villageScene")