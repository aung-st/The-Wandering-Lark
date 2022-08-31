from .Object import Object

import pygame


class Image(Object):
    
    def __init__(self,
                 pos,
                 file_path):
        
        # Add way to set size
        super().__init__(pos)
        
        self.picture = pygame.image.load(file_path)
        self.picture = pygame.transform.scale(self.picture, (720,600))
        
    def update(self,
               surface):
        
        surface.blit(self.picture, self.pos)

    def is_mouse_over(self,
                      position):
        
        # Need size of image to do this
        pass

