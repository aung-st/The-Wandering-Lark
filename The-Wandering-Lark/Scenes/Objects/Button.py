import pygame
from .Object import Object
from .Text import Text

class Button(Object):
    def __init__(self, pos, text, on_click=lambda:None, *args, background=()):
        # on_click is the function that gets called when clicking the button
        # args are parameters passed to on_click (can work without this, idk which is best)
        # Todo: background is (r,g,b) if provided. Makes visable box
        super().__init__(pos)
        
        self.on_click = on_click
        self.params = args
        
        self.text = Text(pos, text)
    
    def update(self, surface):
        self.text.update(surface)

    def is_mouse_over(self, position):
        return self.text.is_mouse_over(position)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((720,600))
    main_font = pygame.font.SysFont("cambria",50)

    button = Button(300,300,"Balls")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.check_for_input(pygame.mouse.get_pos())
            
            screen.fill("Black")
            button.update()
            pygame.display.update()
    
    
