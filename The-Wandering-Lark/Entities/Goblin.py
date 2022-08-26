from .Enemy import Enemy

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", (150, 600), (2, 3), (1,5),(1,9))
        self.level = 1


