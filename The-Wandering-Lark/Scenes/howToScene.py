from .Scene import Scene
from .Objects import *

class howToScene(Scene):
    def __init__(self, surface):
        super().__init__(surface)

        self.add_object(Text((10,20), "Enter: Change Scenes", font_size=35,align="left"))
        self.add_object(Text((10,55), "A: Attack", font_size=35,align="left"))
        self.add_object(Text((10,90), "D: Defend", font_size=35,align="left"))
        self.add_object(Text((10,125), "R: Run", font_size=35,align="left"))
        self.add_object(Text((10,160), "1: Use item 1", font_size=35,align="left"))
        self.add_object(Text((10,195), "2: Use item 2", font_size=35,align="left"))
        self.add_object(Text((10,230), "3: Use item 3", font_size=35,align="left"))
        self.add_object(Text((10,265), "4: Use item 4", font_size=35,align="left"))

        self.add_object(Text((400,20), "5: Use item 5", font_size=35,align="left"))
        self.add_object(Text((400,55), "6: Use item 6", font_size=35,align="left"))
        self.add_object(Text((400,90), "7: Use item 7", font_size=35,align="left"))
        self.add_object(Text((400,125), "8: Use item 8", font_size=35,align="left"))
        self.add_object(Text((400,160), "9: Use item 9", font_size=35,align="left"))
        self.add_object(Text((400,195), "0: Use item 10", font_size=35,align="left"))


    
        
        self.add_object(Button((360,540), "Back", self.change_scene, "main menu"))    



