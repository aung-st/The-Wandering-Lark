from .Object import Object
from .Text import Text

import pygame


class Button(Object):
    
    def __init__(self,
                 pos,
                 text,
                 on_click = lambda: None,
                 *args,
                 background=()):
        
        # on_click is the function that gets called when clicking the button
        # Args are parameters passed to on_click (can work without this, idk which is best)
        # Todo: make background (r,g,b) if provided. Makes visable box
        super().__init__(pos)
        
        self.on_click = on_click
        self.params = args
        
        self.text = Text(pos, text)
    
    def update(self,
               surface):
        
        self.text.update(surface)

    def is_mouse_over(self,
                      position):
        
        return self.text.is_mouse_over(position)



    
    
