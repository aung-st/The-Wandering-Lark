from .Scene import Scene
from .Objects import *

class howToScene(Scene):
    def __init__(self, surface):
        super().__init__(surface)

        self.add_object(Text((10,30), "Enter: Change Scenes", font_size=45,align="left"))
        self.add_object(Text((500,30), "A: Attack", font_size=45,align="left"))
        self.add_object(Text((10,90), "D: Defend", font_size=45,align="left"))
        self.add_object(Text((500,90), "R: Run", font_size=45,align="left"))
        


    
        
        self.add_object(Button((360,540), "Back", self.change_scene, "main menu"))    



