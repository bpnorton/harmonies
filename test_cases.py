"""
Testing!
"""

import game_board_node
import terrain_token

if __name__ == "__main__":
    node = game_board_node.GameBoardNode("TEST")
    node.add_token(terrain_token.TerrainToken(0))
    print(node.to_string())