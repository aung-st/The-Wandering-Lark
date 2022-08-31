from .Scene import Scene
from .Objects import *


class beginScene(Scene):
    
    def __init__(self,
                 surface):
        
        super().__init__(surface)
        
        self.add_object(Text((360,260), "Press Enter to Continue."))
    
    def press(self,
              key):
        
        if key == pygame.K_RETURN: # Remove this if if you don't care what key
            # pygame is imported from .Objects
            self.change_scene("prologue")

