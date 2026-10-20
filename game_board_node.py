"""
Game board node (represents a hexagonal piece of the game board)

"""

import terrain_token

class GameBoardNode:

    def __init__(self, name):
        self.name = name
        self.tokens = [] # The board is empty at the start of the game
        self.animal = None # No animals yet!
        self.neighbors = [None for i in range(6)]

    def add_token(self, token):
        """
        :param token: The player is trying to place a token on the hex
        :return: Whether the token placement was successful
        """
        if self.tokens == []:
            below = -1
        else:
            below = self.tokens[-1].type
        if token.is_placeable(len(self.tokens), below):
            self.tokens.append(token)
            return True
        return False

    def remove_token(self, placed_this_turn):
        """
        :param placed_this_turn: The game state class should keep
        track of the hexes where tokens were placed this turn
        :return: The removed token, if valid
        """
        if self.animal == None and placed_this_turn == True:
            return self.tokens.pop(-1)
        return None

    def add_animal(self, animal):
        pass # TODO: validate animal placement

    def add_neighbor(self, neighbor, direction):
        self.neighbors[direction] = neighbor

    def to_string(self):
        string = self.name
        if self.tokens == []:
            return "Hex " + string + " is empty"
        string += ":"
        for token in self.tokens:
            string += " " + str(token.type.name)
        return "Hex " + string
