"""
Animal Cube
"""

# TODO: Figure out: how are we calculating points from animal cards?
# I believe if we do it based on the cards the player has in their hand, hten
# : the animal cubes themselves will not need to store any point value.

# TODO: Validate placement via terrain_configuration through a place
# function in here?

import animal
import animal_card
from hex import Hex

class AnimalCube:

    def __init__(self):
        self.Hex = None

    def is_placed(self):
        return self.Hex is not None