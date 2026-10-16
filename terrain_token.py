"""
Terrain Token

"""

from enum import Enum

class TerrainType(Enum):
    """
    Encoding terrain type info as ints so it's easier to use
    """
    WATER = 0
    GRASS = 1
    STONE = 2
    WOOD = 3
    LEAVES = 4
    BRICK = 5


terrain_type_info = {
    TerrainType.WATER: [1],
    TerrainType.GRASS: [1],
    TerrainType.STONE: [3, TerrainType.STONE],
    TerrainType.WOOD: [2, TerrainType.WOOD],
    TerrainType.LEAVES: [3, TerrainType.WOOD],
    TerrainType.BRICK: [2, TerrainType.STONE, TerrainType.WOOD, TerrainType.BRICK]
}


class TerrainToken:
    """
    To be placed on the board to create habitats
    Can have one of six types
    """
    def __init__(self, type):
        self.type = TerrainType(type) # An int representing one of 6 terrain types
        # An int representing the max height it can be placed (STARTS AT 1)
        self.max_height = terrain_type_info[self.type.value][0]
        if len(terrain_type_info[type]) > 1:
            # A list of terrain types it can be placed on
            self.placeable_on = terrain_type_info[type][1:]
        else:
            self.placeable_on = []

    def is_placeable(self, height, type_below):
        """
        :param height: How many tokens are already on the hex
        :param type_below: What terrain type if any is on top
        :return: Whether the token can be placed on the hex
        """
        if height == 0:
            return True
        if height < self.max_height and type_below in self.placeable_on:
            return True
        return False
