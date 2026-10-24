"""
Create terrain configurations for animal habitats and other structures.
"""

# TODO: test cases!!! this is all unvalidated so far
# TODO: Pylint
# TODO: Consider the river?
# TODO: Consider using a dictionary for the pattern, to name each position rather than relying on arbitrary index orders.

from terrain_token import TerrainToken
from hex import Hex
from enum import Enum, auto

class TerrainPattern(Enum):
    """
    Encoding terrain pattern so they're easy to call upon
    """
    LINE2 = auto()
    LINE3 = auto()
    DIAMOND = auto()
    HAT = auto()


class TerrainConfiguration:
    """
    To be checked to validate proper habitats for an animal to be placed
    """

    def __init__(self, pattern: TerrainPattern, required_tokens: list[list[TerrainToken]]):
        # A TerrainPattern representing one of the 4 terrain patterns
        self.pattern = pattern
        """
        A list containing lists of TerrainTokens, to determine what the animal's
        habitat should look like. The order of the list should be based on the following pattern:
        LINE2: [AnimalCube Token, Adjacent Token]
        LINE3: [AnimalCube Token, Adjacent Token, End Token]
        DIAMOND: [AnimalCube Token, Adjacent Token 1, Adjacent Token 2, Adjacent Token 3]
        (for DIAMOND, aside from the AnimalCube Token the order really does not matter, as all of them are the same)
        HAT: [AnimalCube Token, Adjacent Token 1, Adjacent Token 2]
        (for HAT, aside from the AnimalCube Token, the order really does not matter, as both of them are the same)
        """
        self.required_tokens = required_tokens

    def validate(self, target_hex):
        """
        param: target_hex: The hex for the Animal Cube to be placed on
        return: Whether the Animal Cube can be placed on the hex
        """
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
        """
        param: hex: The hex to be checked against the required pattern
        param: index: The index of the required pattern to be checked
        """
        return hex is not None and hex.tokens == self.required_tokens[index]

    # TODO: add comments to explain logic for the following validations

    def validate_line2(self, target_hex):
        if self.matches(target_hex, 0):
            for neighbor in target_hex.neighbors:
                if self.matches(neighbor, 1):
                    return True
        return False
    
    def validate_line3(self, target_hex):
        if self.matches(target_hex, 0):
            for index, neighbor in enumerate(target_hex.neighbors):
                if self.matches(neighbor, 1):
                    if self.matches(neighbor.neighbors[index], 2):
                        return True
        return False

    def validate_hat(self, target_hex):
        if self.matches(target_hex, 0):
            for index, neighbor in enumerate(target_hex.neighbors):
                if self.matches(neighbor, 1):
                    if self.matches(target_hex.neighbors[(index + 2) % 6], 2):
                        return True
        return False

    def validate_diamond(self, target_hex):
        if self.matches(target_hex, 0):
            for index, neighbor in enumerate(target_hex.neighbors):
                if self.matches(neighbor, 1):
                    if (self.matches(target_hex.neighbors[(index + 1) % 6], 2) 
                                    and self.matches(target_hex.neighbors[(index + 2) % 6], 3)):
                        return True
        return False
