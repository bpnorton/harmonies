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

    def __init__(self, pattern: TerrainPattern, required_tokens: list[list[TerrainToken]]):
        self.pattern = pattern
        self.required_tokens = required_tokens

    def validate(self, target_hex):
        match self.pattern:
            case TerrainPattern.LINE2:
                return self.validate_line2(target_hex)
            case TerrainPattern.LINE3:
                return self.validate_line3(target_hex)
            case TerrainPattern.DIAMOND:
                return self.validate_diamond(target_hex)
            case TerrainPattern.HAT:
                return self.validate_hat(target_hex)
        return False

    def matches(self, hex: Hex | None, index: int):
        return hex.tokens == self.required_tokens[index] and hex is not None

    def validate_line2(self, target_hex):
        if target_hex.tokens == self.required_tokens[0]:
            for neighbor in target_hex.neighbors:
                if neighbor.tokens == self.required_tokens[1]:
                    return True
        return False
    
    def validate_line3(self, target_hex):
        if target_hex.tokens == self.required_tokens[0]:
            for index, neighbor in enumerate(target_hex.neighbors):
                if neighbor.tokens == self.required_tokens[1]:
                    if neighbor.neighbors[index].tokens == self.required_tokens[2]:
                        return True
        return False

    def validate_hat(self, target_hex):
        if target_hex.tokens == self.required_tokens[0]:
            for index, neighbor in enumerate(target_hex.neighbors):
                if neighbor.tokens == self.required_tokens[1]:
                    if target_hex.neighbors[(index + 2) % 6].tokens == self.required_tokens[2]:
                        return True
        return False

    def validate_diamond(self, target_hex):
        if target_hex.tokens == self.required_tokens[0]:
            for index, neighbor in enumerate(target_hex.neighbors):
                if neighbor is not None and neighbor.tokens == self.required_tokens[1]:
                    if (target_hex.neighbors[(index + 1) % 6].tokens == self.required_tokens[2] 
                        and target_hex.neighbors[(index + 2) % 6].tokens == self.required_tokens[3]):
                        return True
        return False
