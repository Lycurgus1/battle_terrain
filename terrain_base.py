from abc import *

class Terrain:

    def __init__(self):
        pass

    @abstractmethod
    def combat_width(self):
        pass

    @abstractmethod
    def army_effects(self):
        pass