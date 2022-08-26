import pygame
from .Object import Object

class Text(Object):
    def __init__(self, pos, text, font_size=50, align="centre"):
        super().__init__(pos)

        # Todo: make font, size, color etc changable based on parameters
        # Text probably needs a bit of work but cba rn
        self.font = pygame.font.SysFont('Corbel', font_size)
        self.align = align

        self.set_text(text)
    
    def update(self, surface):
        surface.blit(self.text, self.text_rectangle)

    def is_mouse_over(self, position):
        return position[0] in range(self.text_rectangle.left,
                                    self.text_rectangle.right) \
            and position[1] in range (self.text_rectangle.top,
                                      self.text_rectangle.bottom)

    def set_text(self, text):
        self.text = text
        self.text = self.font.render(self.text, True, "White")
        self.text_rectangle = self.text.get_rect(center = (self.x,self.y))
        left = self.text_rectangle.left
        right = self.text_rectangle.right

        if self.align == "left":
            self.text_rectangle = self.text.get_rect(center = (right, self.y))
        elif self.align == "right":
            self.text_rectangle = self.text.get_rect(center = (left, self.y))
    
