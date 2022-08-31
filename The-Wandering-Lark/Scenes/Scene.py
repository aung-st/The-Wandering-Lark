import pygame


class Scene:

    def __init__(self, 
                 surface):

        self.objects = [] # Can't think of a better name. Things to draw basically
        self.surface = surface

        # change_to changes when switching to a new screen
        self.change = False
        self.change_to = ""

        self.exit = False

    def add_object(self, 
                   _object): # object is already a used word in python

        self.objects.append(_object)

    def update(self):

        self.per_frame()
        
        for _object in self.objects:
            _object.update(self.surface)

    def per_frame(self):
        
        pass

    def click(self, 
              pos): # Called on mouse click

        for _object in self.objects:
            if _object.is_mouse_over(pos):
                _object.on_click(*_object.params)

    def press(self, 
              key): # Called on any keypress
        
        pass

    def change_scene(self,
                     new_screen): # Call (from button) to change scenes
        
        self.change_to = new_screen
        self.change = True

    def reset(self):
        
        pass



















if __name__ == "__main__":
    #menu = menu()
    #menu.launch()
    pass
