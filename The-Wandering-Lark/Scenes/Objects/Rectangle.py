import pygame
from .Object import Object

class Rectangle(Object):
    def __init__(self, pos, size, colour=(255,255,255)):
        super().__init__(pos)

        self.pos = pos
        self.width, self.height = size
        self.size = size
        self.colour = colour
        
    def update(self, surface):
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.height))

    def is_mouse_over(self, position):
        return self.x < position[0] < self.x+self.width and self.y < position[1] < self.y+self.height

    def set_pos(self, x, y):
        self.pos = (x,y)
