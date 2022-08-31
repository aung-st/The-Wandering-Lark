from .Scene import Scene
from .Objects import *


class prologueScene(Scene):

    def __init__(self, 
                 surface):

        super().__init__(surface)

        story = """
        Life in the kingdom of Gevel has been tumultous at best. 
        Many a field lay dry for several seasons, unable to sprout anything.
        Monsters scourge not only villages, but even walled towns.
        You grew up in one of said villages, and were one of 
        the lucky few who managed to reach adulthood, in one piece and
        healthy by the standards of impoverished villages anyway. 
        Even in spite of all the monster raids, bandits, and then some.

        In the hopes of finding any kind of opportunity elsewhere, 
        you decided one day, that it was time to leave your village.
        With nothing but the clothes on your person, a piece of bread as hard
        as any rock, and a tiny canteen of water, and a wooden club to defend yourself with.

        For many weeks you wandered farther and farther from your former home, 
        subsisting off of whatever edible morsel nature is willing to bestow upon you,
        and the occassional scavenge from the corpse of some unlucky fellow.

        You eventually find yourself in yet another forest path.
        You have no more food, nor water, and it is pitch black.
        It's also rather chilly for a person wearing nothing but rags.
        
        Suddenly you hear growling...
        A pack of goblins are out hunting for something. 
        There is no choice. You grab your club and steel yourself.
        It is either you or them, and quite frankly you'd feel rather
        annoyed to die at the hands of some goblins, on an empty stomach.

        "Time to find out if I'll regret all this...", you mutter."""

        story = story.split("\n")
        line_gap = 20
        y = 5

        for line in story:
            self.add_object(Text((5,y), line, font_size = 20, align = "left"))
            y += line_gap
        
    def press(self, key):
        if key == pygame.K_RETURN:
            self.change_scene("prologueFight")
