from Scenes import *
from Entities import Player

import pygame


def main():
    pygame.init()
    pygame.display.set_caption("The Wandering Lark")
    
    resolution = (720,600)
    surface = pygame.display.set_mode(resolution)
    player = Player("Caleb")
    scenes = {"main menu": menuScene(surface),
              "begin": beginScene(surface),
              "prologue": prologueScene(surface),
              "prologueFight": prologueFight(surface, 5, player),
              "prologueEnd": prologueEnd(surface),
              "villageScene": villageScene(surface),
              "caerham": caerham(surface),
              "gameoverScene": gameoverScene(surface),
              "inn": inn(surface, player),
              "patrol": patrol(surface, 5, player),
              "harveys": harveysHouse(surface),
              "howToScene": howToScene(surface),
              "credits": credits(surface)}
    
    current_scene = scenes["main menu"]    
    running = True
    while running:
        surface.fill((0,0,0))
        current_scene.update()
        pygame.display.update()

        running = not current_scene.exit

        if current_scene.change:
            current_scene.change = False
            if current_scene.change_to in scenes:
                current_scene = scenes[current_scene.change_to]
            else:
                print("error when changing scene")
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_scene.click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                current_scene.press(event.key)
                
    pygame.quit()
    

if __name__ == "__main__":
    main()
