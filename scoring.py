from player import Player
from game_board import GameBoard
from gui import GameWindow

# should players have a game_board rather than a game_window, and each function in game_state is passed the 
# player that it wants as well as the game board? i have to check what is in game state more

player = Player('player1', [], [])
game_board = player.game_board


def score_game(player: Player, game_board: GameBoard):
    total_score = 0
    scored_grass_coordinates = []
    longest_river = 0
    for hex in game_board.hexes:
        tokens = [token.type.value for token in hex.tokens]

        # basic token scores for 1 hex configurations
        if tokens == [4] or tokens == [2]:
            total_score += 1
        if tokens == [3, 4] or tokens == [2, 2]:
            total_score += 3
        if tokens == [3, 3, 4] or tokens == [2, 2, 2]:
            total_score += 7

        # this needs to repeat itself, find the entire connection of the fields
        # river one will need to do the same
        if tokens == [1] and hex.coordinates not in scored_grass_coordinates:
            grass_tokens = [hex]
            scored_grass_coordinates.append(hex.coordinates)
            for grass_token in grass_tokens:
                for neighbor in grass_token.neighbors:
                    if neighbor.type.value == [1] and neighbor.coordinates not in scored_grass_coordinates:
                        grass_tokens.append(neighbor)
                        scored_grass_coordinates.append(neighbor.coordinates)
                grass_tokens.remove(grass_token)
            total_score += 5

        # score for 'houses'
        if tokens == [2, 5] or tokens == [5, 5] or tokens == [3, 5]:
            neighbor_types = []
            for neighbor in hex.neighbors:
                if neighbor.tokens.type.value not in neighbor_types:
                    neighbor_types.append(neighbor.tokens.type.value)
            if len(neighbor_types) >= 3:
                total_score += 5

        # Score the river using coordinate distances apart

        if tokens == [0]:
            water_coordinates = [hex.coordinates]
            water_tokens = [hex]
            for water_token in water_tokens:
                for neighbor in water_token.neighbors:
                    if neighbor.type.value == [0] and neighbor.coordinates not in water_coordinates:
                        water_tokens.append(neighbor)
                        water_coordinates.append(neighbor.coordinates)
                    water_tokens.remove(water_token)

            for coords1 in water_coordinates:
                for coords2 in water_coordinates:
                    distance_apart = abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])
                    longest_river = max(longest_river, distance_apart)
                    river_pair = (coords1, coords2)

        if longest_river == 2:
            total_score += 2
        elif longest_river == 3:
            total_score += 5
        elif longest_river == 4:
            total_score += 8
        elif longest_river == 5:
            total_score += 11
        elif longest_river == 6:
            total_score += 15
        elif longest_river >= 7:
            total_score += 15 + ((longest_river - 6) * 4)

            





score_game(player, game_board)
# def score_game(player, game_window):
#     print(game_window.game_board)


# player = Player('player1', [], [])
# game_window = GameWindow()


# score_game(player, game_window)