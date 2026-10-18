"""
Animal Card
"""

import animal
import animal_cube

class AnimalCard:

    def __init__(self, animal, point_values):
        self.point_values = point_values  # Tuple of integer point values, e.g. (5, 11)
        self.animal = animal # An Animal object
        self.animal_cubes = []
        for val in self.point_values:
