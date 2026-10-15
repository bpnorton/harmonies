"""
Terrain Token

"""

from enum import Enum

class TerrainType(Enum):
    WATER = 0
    GRASS = 1
    STONE = 2
    WOOD = 3
    LEAVES = 4
    BRICK = 5


terrain_type_info = {
    "water": [1],
    "grass": [1],
    "stone": [3, TerrainType.STONE],
    "wood": [2, TerrainType.WOOD],
    "leaves": [3, TerrainType.WOOD],
    "brick": [2, TerrainType.STONE, TerrainType.WOOD, TerrainType.BRICK]
}

class TerrainToken:

    def __init__(self, type):
        self.type = type # A string, e.g. "wood"
        self.max_height = terrain_type_info[type][0] # An int representing the max height it can be placed (STARTS AT 1)
        if len(terrain_type_info[type]) > 1:
            self.placeable_on = terrain_type_info[type][1:] # A list of terrain types it can be placed on
        else:
            self.placeable_on = []
