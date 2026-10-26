"""
The Game State
"""

import terrain_token
import random

# Game Loop

class GameLoop:
    def __init__(self, players):
        # a player object
        self.player = players
        # the bag of tokens
        self.tokens = [] # empty until function is called
        self.deck = [] # empty until function called
        # the num of available spaces on the board
        self.board_spaces = 23 # the board has 23 spaces
        # the list which holds the points of everything a player has
        self.score_lst = []

    # fill tokens list with number of tokens allowed in game
    def fill_bag(self, tokens):
        # water tokens
        for _ in range(0, 23):
            tokens.append(terrain_token.TerrainToken(0))

        # grass/fields tokens
        for _ in range(0, 19):
            tokens.append(terrain_token.TerrainToken(1))
            
        # stone tokens
        for _ in range(0, 23):
            tokens.append(terrain_token.TerrainToken(2))

        # wood tokens
        for _ in range(0, 21):
            tokens.append(terrain_token.TerrainToken(3))

        # leaves tokens
        for _ in range(0, 19):
            tokens.append(terrain_token.TerrainToken(4))

        # brick tokens
        for _ in range(0, 15):
            tokens.append(terrain_token.TerrainToken(5))

    # add tokens to pentagon board thing
    def fill_pentagon(self, tokens):
        random.shuffle(tokens)

    # fill deck with cards allowed in game
    def fill_deck(self, deck):
        pass # import JSON file!!!

    # uses current player and goes through steps of a turn
    def current_turn(self, player):
        pass

    # changing from one player to another
    def change_turn(self, player):
        pass

    # called at end of game to sum up totals
    def score_points(self, score_lst):
        # call score.py!
        pass

    # what happens when no tokens are left or no spaces on the board are left
    def end_game(self, tokens, board_spaces):
        pass