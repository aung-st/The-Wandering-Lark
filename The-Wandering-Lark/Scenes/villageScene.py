from .Scene import Scene
from .Objects import *

class villageScene(Scene):

    def __init__(self, 
                 surface):

        super().__init__(surface)

        story = """
        You wake up, except you're laying down on a bed. A soft, comfy bed. The last 
        time you found yourself feeling any semblence of comfort would have been in 
        your old village. 

        "Look who's finally up! Don't you worry, I've patched you right up!", the
        burly man said excitely. 

        "How long has it been?", You ask.

        "Oh only been a couple days.", he replies.

        You groan, "You know, you're awfully calm for someone who saw a man waltz
        in almost dead!"

        He laughs, "Harvey's the name! I'm the village watchman! What do I call 
        you now anyways?".

        You glare at him. It seems like Harvey didn't register what you actually said
        to him at all. 

        "Caleb", You reply with a sharp tone, "Now can you tell me where I-"

        "You know, we could use a bit of help around here. Those damn goblins do give us
        a headache from time to time you know. 
        Can't bloody go anywhere because of them, and sometimes they'll send raiding
        parties!". 

        You let out a long sigh. Not even a minute after regaining conciousness, you find
        yourself already burdened with tasks. 
        
        "Oh and Caleb? Welcome to Caerham", Harvey says with a giant toothy grin.
        """
        
        story = story.split("\n")
        line_gap = 20
        y = 5

        for line in story:
            self.add_object(Text((5,y), line, font_size=20, align = "left"))
            y += line_gap
        
    def press(self, 
              key):

        if key == pygame.K_RETURN:
            self.change_scene("caerham")