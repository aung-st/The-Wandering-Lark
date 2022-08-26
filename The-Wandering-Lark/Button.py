import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((720,600))
main_font = pygame.font.SysFont("cambria",50)
class Button: 
    def __init__(self,x,y,text_input):
        self.x = x
        self.y = y
        self.text_input = text_input
        self.text = main_font.render(self.text_input,True,"White")
        self.text_rectangle = self.text.get_rect(center = (self.x,self.y))
    
    def update(self):
        screen.blit(self.text, self.text_rectangle)

    def check_for_input(self, position):
        if position[0] in range(self.text_rectangle.left,self.text_rectangle.right) and position[1] in range (self.text_rectangle.top, self.text_rectangle.bottom):
            return True
        return False

if __name__ == "__main__":
    button = Button(300,300,"Balls")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.check_for_input(pygame.mouse.get_pos())
            
            screen.fill("Black")
            button.update()
            pygame.display.update()
    
    