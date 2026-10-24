"""
The Game State
"""

# Game Loop

class game_loop:
    def __init__(self, player, score_lst):
        # a player object
        self.player = player
        # the bag of tokens
        self.tokens = [] # empty until function is called
        self.deck = [] # empty until function called
        # the num of available spaces on the board
        self.board_spaces = 23 # the board has 23 spaces
        # the list which holds the points of everything a player has
        self.score_lst = score_lst

    # fill tokens list with number of tokens allowed in game
    def fill_bag(self, tokens):
        pass

    # fill deck with cards allowed in game
    def fill_deck(self, deck):
        pass

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