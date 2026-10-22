"""
Animal

"""

class Animal:

    def __init__(self, name, sprite_img, terrain_config, point_values):
        self.name = name # A string, e.g. "Grizzly Bear"
        self.sprite_img = sprite_img # A string, e.g. "./Sprites/GrizzlyBear.png"
        self.terrain_config = terrain_config # Terrain configuration for valid habitat (FIGURE OUT STRUCTURE)
