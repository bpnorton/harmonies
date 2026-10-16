"""
Testing!
"""

import game_board_node as gbn
import terrain_token as tt

if __name__ == "__main__":
    node = gbn.GameBoardNode("TEST")
    print(node.to_string())
    node.add_token(tt.TerrainToken(0))
    print(node.to_string())