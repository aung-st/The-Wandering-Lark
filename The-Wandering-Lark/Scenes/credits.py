from .Scene import Scene
from .Objects import *

class credits(Scene):
    def __init__(self, surface):
        super().__init__(surface)
        
        
        self.add_object(Text((360,30), "Art and Story", font_size=40))
        self.add_object(Text((360,70), "aung-st", font_size=30))

        self.add_object(Text((360,140), "Programming", font_size=40))
        self.add_object(Text((360,180), "NE0NGH0ST", font_size=30))
        self.add_object(Text((360,210), "aung-st", font_size=30))

        self.add_object(Text((360,280), "Audio (Or lack thereof)", font_size=40))
        self.add_object(Text((360,320), "Everybody", font_size=30))



        self.add_object(Button((360,540), "Back", self.change_scene, "main menu"))    

