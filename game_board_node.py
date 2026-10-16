"""
Game board node (represents a hexagonal piece of the game board)

"""

import terrain_token

class GameBoardNode:

    def __init__(self, name):
        self.name = name
        self.tokens = [] # The board is empty at the start of the game
        self.neighbors = [] # TODO: when creating graph, add neighbors - should end up with a list of 6 GameBoardNodes (some None)

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

    def add_animal(self, animal):
        pass # TODO: validate animal placement

    def to_string(self):
        string = self.name
        if self.tokens == []:
            return "Hex " + string + " is empty"
        string += ":"
        for token in self.tokens:
            string += " " + str(token.type)
        return "Hex " + string
