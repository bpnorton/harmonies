"""
The Game State
"""

# Game Loop

class game_loop:
    def __init__(self, player, score_lst):
        # a player object
        self.player = player
        # the bag of tokens
        self.tokens = [] #TODO: Replace with list of all tokens in game
        # the num of available spaces on the board
        self.board = 23 # the board has 23 spaces
        # the list which holds the points of everything a player has
        self.score_lst = score_lst

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

    def end_game(self, tokens, board):
        pass