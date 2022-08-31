from .Scene import Scene
from .Objects import *


class gameoverScene(Scene):
    
    def __init__(self,
                 surface):
        
        super().__init__(surface)

        # Initialize text 
        self.top_message = Text((360,160), "", font_size = 30)
        self.bottom_message = Text((360,200), "", font_size = 20)

        # Add text
        self.top_message.set_text("GAME OVER")
        self.bottom_message.set_text("Press enter to return to main menu")

        # Render text
        self.add_object(self.top_message)
        self.add_object(self.bottom_message)

    def press(self,
              key):
        
        if key == pygame.K_RETURN:
            self.change_scene("main menu")
