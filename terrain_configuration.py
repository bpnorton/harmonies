"""
Create terrain configurations for animal habitats and other structures.
"""

# TODO: Consider the river?
# TODO: Validate heights
# TODO: I think this should be hexes

from terrain_token import TerrainType
from terrain_token import TerrainToken
from hex import Hex
# enum for each different type of 'shape' of terrain
from enum import Enum, auto

class TerrainPattern(Enum):
    LINE2 = auto()
    LINE3 = auto()
    DIAMOND = auto()
    HAT = auto()

# terrain configurations will be in relation to where the animal cube is placed

class TerrainConfiguration:

    def __init__(self, pattern: TerrainPattern, required_tokens: list[TerrainToken]):
        self.pattern = pattern
        self.required_tokens = required_tokens

    def validate(self, target_token):
        match self.pattern:
            case TerrainPattern.LINE2:
                return self.validate_line2(target_token)
            case TerrainPattern.LINE3:
                return self.validate_line3(target_token)
            case TerrainPattern.DIAMOND:
                return self.validate_diamond(target_token)
            case TerrainPattern.HAT:
                return self.validate_hat(target_token)
        return False

    def validate_line2(self, target_token):
        if target_token == self.required_tokens[0]:
            for neighbor in target_token.neighbors:
                if neighbor == self.required_tokens[1]:
                    return True
        return False
    
    def validate_line3(self, target_token):
        if target_token == self.required_tokens[0]:
            for index, neighbor in enumerate(target_token.neighbors):
                if neighbor == self.required_tokens[1]:
                    if neighbor.neighbors[index] == self.required_tokens[2]:
                        return True
        return False

    def validate_hat(self, target_token):
        if target_token == self.required_tokens[0]:
            for index, neighbor in enumerate(target_token.neighbors):
                if neighbor == self.required_tokens[1]:
                    if target_token.neighbors[(index + 2) % 6] == self.required_tokens[2]:
                        return True
        return False

    def validate_diamond(self, target_token):
        if target_token == self.required_tokens[0]:
            for index, neighbor in enumerate(target_token.neighbors):
                if neighbor == self.required_tokens[1]:
                    if (target_token.neighbors[(index + 1) % 6] == self.required_tokens[2] 
                        and target_token.neighbors[(index + 2) % 6] == self.required_tokens[3]):
                        return True
        return False
