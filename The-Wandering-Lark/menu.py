import pygame
from pygame.locals import *
from sys import exit 
from Button import Button
#from Prologue import prologue
class menu:
    def __init__(self):  
        #intialize session and values
        pygame.init()
        pygame.display.set_caption('shittyroguelike')

        self._running = True
        self.display_surf = None
        self.resolution = (720,600)
        self.color = (21,71,52)

        self.font = pygame.font.SysFont('Corbel',50) 
        self.display_surf = pygame.display.set_mode(self.resolution)
        self._running = True
    
    def render_text(self,text,font,text_color, x,y):
        self.text = font.render(text,True,text_color)
        self.display_surf.blit(self.text,(x,y))
   
    def on_event(self,event):
        #if all events could be put into this method rather than inside the launch sequence that would be nice
        if event.type == pygame.QUIT:
            self._running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.Start.check_for_input(self.PLAY_MOUSE_POS):
                self.play()
  

    def quit(self):
        pygame.quit()
        exit() #so it actually quits properly

    def play(self):
        #that's what she said
        
        while True:
            self.display_surf.fill("black")
            PLAY_TEXT = self.font.render("Press Enter to Continue.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(360, 260))
            self.display_surf.blit(PLAY_TEXT, PLAY_RECT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() 
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RETURN: 
                        self.intro()
                        
            pygame.display.update()



    def intro(self):
        self.paragraph_font = pygame.font.SysFont('Corbel',20)
        message1_1 = "Life in the kingdom of Gevel has been tumultous at best. Many a field"
        message1_2 = "lay dry for several seasons, unable to sprout anything."
        message1_3 = "Monsters scourge not only villages, but even walled towns."
        message1_4=  "You grew up in one of said villages. One of the lucky few"
        message1_5 = "who managed to reach adulthood in spite of monster raids, bandits, and then some." 
        

        message2_1 = "In hope to find any kind of opportunity, you decided to leave your village,"
        message2_2 = "with nothing but the clothes on your person, a piece of bread as hard "
        message2_3 = "as any rock, and a tiny canteen of water, and a wooden club to defend yourself with."
        message2_4 = "You wander for many weeks, subsisting off of whatever"
        message2_5 = "edible fruit nature is willing to bestow upon you, and any"
        message2_6 = "possessions that remain of the occassional dead bodies you find laying around."
      

        message3_1 = "You eventually find yourself in yet another forest path. "
        message3_2 = "You have no food, no water, and it is pitch black."
        message3_3 = "Suddenly you hear growling..."
        message3_4 = "A pack of goblins are out hunting for something. There is no choice, you grab your club."
        message3_5 = "\"Perhaps leaving the village was a mistake.\", you say to yourself."

        PROLOGUE_TEXT1_1 = self.paragraph_font.render(message1_1, True, "White")
        PROLOGUE_RECT1_1 = PROLOGUE_TEXT1_1.get_rect(center=(360, 60))
        PROLOGUE_TEXT1_2 = self.paragraph_font.render(message1_2, True, "White")
        PROLOGUE_RECT1_2 = PROLOGUE_TEXT1_2.get_rect(center=(360, 80))
        PROLOGUE_TEXT1_3 = self.paragraph_font.render(message1_3, True, "White")
        PROLOGUE_RECT1_3 = PROLOGUE_TEXT1_3.get_rect(center=(360, 100))
        PROLOGUE_TEXT1_4 = self.paragraph_font.render(message1_4, True, "White")
        PROLOGUE_RECT1_4 = PROLOGUE_TEXT1_4.get_rect(center=(360, 120))
        PROLOGUE_TEXT1_5 = self.paragraph_font.render(message1_5, True, "White")
        PROLOGUE_RECT1_5 = PROLOGUE_TEXT1_5.get_rect(center=(360, 140))

        PROLOGUE_TEXT2_1 = self.paragraph_font.render(message2_1, True, "White")
        PROLOGUE_RECT2_1 = PROLOGUE_TEXT2_1.get_rect(center=(360, 180))
        PROLOGUE_TEXT2_2 = self.paragraph_font.render(message2_2, True, "White")
        PROLOGUE_RECT2_2 = PROLOGUE_TEXT2_2.get_rect(center=(360, 200))
        PROLOGUE_TEXT2_3 = self.paragraph_font.render(message2_3, True, "White")
        PROLOGUE_RECT2_3 = PROLOGUE_TEXT2_3.get_rect(center=(360, 220))
        PROLOGUE_TEXT2_4 = self.paragraph_font.render(message2_4, True, "White")
        PROLOGUE_RECT2_4 = PROLOGUE_TEXT2_4.get_rect(center=(360, 240))
        PROLOGUE_TEXT2_5 = self.paragraph_font.render(message2_5, True, "White")
        PROLOGUE_RECT2_5 = PROLOGUE_TEXT2_5.get_rect(center=(360, 260))
        PROLOGUE_TEXT2_6 = self.paragraph_font.render(message2_6, True, "White")
        PROLOGUE_RECT2_6 = PROLOGUE_TEXT2_6.get_rect(center=(360, 280))

        PROLOGUE_TEXT3_1 = self.paragraph_font.render(message3_1, True, "White")
        PROLOGUE_RECT3_1 = PROLOGUE_TEXT3_1.get_rect(center=(360, 320))
        PROLOGUE_TEXT3_2 = self.paragraph_font.render(message3_2, True, "White")
        PROLOGUE_RECT3_2 = PROLOGUE_TEXT3_2.get_rect(center=(360, 340))
        PROLOGUE_TEXT3_3 = self.paragraph_font.render(message3_3, True, "White")
        PROLOGUE_RECT3_3 = PROLOGUE_TEXT3_3.get_rect(center=(360, 360))
        PROLOGUE_TEXT3_4 = self.paragraph_font.render(message3_4, True, "White")
        PROLOGUE_RECT3_4 = PROLOGUE_TEXT3_4.get_rect(center=(360, 380))
        PROLOGUE_TEXT3_5 = self.paragraph_font.render(message3_5, True, "White")
        PROLOGUE_RECT3_5 = PROLOGUE_TEXT3_5.get_rect(center=(360, 400))


        


        while True:
            for event in pygame.event.get():
                    self.display_surf.fill("black")
                    self.display_surf.blit(PROLOGUE_TEXT1_1, PROLOGUE_RECT1_1)
                    self.display_surf.blit(PROLOGUE_TEXT1_2, PROLOGUE_RECT1_2)
                    self.display_surf.blit(PROLOGUE_TEXT1_3, PROLOGUE_RECT1_3)
                    self.display_surf.blit(PROLOGUE_TEXT1_4, PROLOGUE_RECT1_4)
                    self.display_surf.blit(PROLOGUE_TEXT1_5, PROLOGUE_RECT1_5)

                    self.display_surf.blit(PROLOGUE_TEXT2_1, PROLOGUE_RECT2_1)
                    self.display_surf.blit(PROLOGUE_TEXT2_2, PROLOGUE_RECT2_2)
                    self.display_surf.blit(PROLOGUE_TEXT2_3, PROLOGUE_RECT2_3)
                    self.display_surf.blit(PROLOGUE_TEXT2_4, PROLOGUE_RECT2_4)
                    self.display_surf.blit(PROLOGUE_TEXT2_5, PROLOGUE_RECT2_5)
                    self.display_surf.blit(PROLOGUE_TEXT2_6, PROLOGUE_RECT2_6)

                    self.display_surf.blit(PROLOGUE_TEXT3_1, PROLOGUE_RECT3_1)
                    self.display_surf.blit(PROLOGUE_TEXT3_2, PROLOGUE_RECT3_2)
                    self.display_surf.blit(PROLOGUE_TEXT3_3, PROLOGUE_RECT3_3)
                    self.display_surf.blit(PROLOGUE_TEXT3_4, PROLOGUE_RECT3_4)
                    self.display_surf.blit(PROLOGUE_TEXT3_5, PROLOGUE_RECT3_5)




                    if event.type == pygame.QUIT:
                        self.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:   
                            pass
                    pygame.display.update()


    def launch(self):  

        while (True): 
            self.MENU_MOUSE_POSITION = pygame.mouse.get_pos()
            MENU_TEXT = self.font.render("MAIN MENU", True, "White")
            MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))
            self.display_surf.blit(MENU_TEXT,MENU_RECT)

            self.Start = Button(360,160,"Start")
            self.Load = Button(360,220,"Load")
            self.Options = Button(360,280,"Options")
            self.Credits = Button(360,340,"Credits")
            self.Quit = Button(360,400,"Quit")

            for button in [self.Start,self.Load,self.Options,self.Credits,self.Quit]:
                button.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.Start.check_for_input(self.MENU_MOUSE_POSITION):
                        self.play()
                    if self.Quit.check_for_input(self.MENU_MOUSE_POSITION):
                        self.quit()
            
            

            pygame.display.update()
        
        
        


if __name__ == "__main__":
    menu = menu()
    menu.launch()