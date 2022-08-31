from .Scene import Scene
from .Objects import *

class menuScene(Scene):
    def __init__(self, surface):
        
        super().__init__(surface)

        self.add_object(Text((360,75), "MAIN MENU"))
        
        self.add_object(Button((360,160), "Start", self.change_scene, "begin"))
        self.add_object(Button((360,220), "How to play", self.how_to_play))
        self.add_object(Button((360,280), "Credits", self.credits))
        self.add_object(Button((360,340), "Quit", self.quit))

    def start(self):
        self.change_screen("begin")

    def how_to_play(self):
        self.change_scene("howToScene")

    def credits(self):
        self.change_scene("credits")

    def quit(self):
        self.exit = True
