from Entities import Player
class Healing_Potion():
    def __init__(self):
        self.name = "Healing Potion"
        self.value = 30

    def use(self):
        self.healing = 50
        Player.heal(self.healing)
        return self.healing

