"""
Player
"""

import gui
import animal_card

class Player:
    def __init__(self, name, deck, tokens):
        # name of the player
        self.name = name
        # the list of cards in the deck (from game_state)
        self.deck = deck
        # a list of tokens the player currently has (from game_state)
        self.tokens = tokens
        # a list of cards the player has not completed
        self.uncompleted_cards = [] # player starts with no cards
        # a list of cards the player has completed
        self.completed_cards = [] # player starts with no completed cards

        self.game_window - gui.GameWindow()

    # player takes a card from the deck
    def take_card(self, deck):
        pass

    # player takes tokens from wheel and replaces them
    def grab_tokens(self, tokens):
        pass

    # player places cubes on board
    def place_cube(self, uncompleted_cards):
        pass

    # recording the scores of each card completed
    def record_score(self, completed_cards):
        pass