import pygame

class Object: 
    def __init__(self, pos):
        self.params = ()
        
        self.x, self.y = pos
        self.pos = pos
    
    def update(self, surface):
        pass

    def is_mouse_over(self, position):
        return False

    def on_click(self, *args):
        pass

