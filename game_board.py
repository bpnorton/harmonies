"""
Logical representation of game board
"""

import game_board_node as gbn

COORDINATES = [(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),
               (-1,2),(0,2),(1,2),(2,2),(3,2),(-1,3),(0,3),(1,3),(2,3),
               (-2,4),(-1,4),(0,4),(1,4),(2,4)]


def add_link(node1, node2, direction):
    node1.add_neighbor(node2, direction)
    node2.add_neighbor(node1, (direction + 3)%6)


class GameBoard:

    def __init__(self):
        self.nodes = []
        for i in range(23):
            self.nodes.append(gbn.GameBoardNode("n"+str(i), COORDINATES[i]))

        # Add edges: 0 = West, increasing clockwise until 5 = SW
        # Horizontals
        for i in range(22):
            if i not in [4,8,13,17]:
                add_link(self.nodes[i], self.nodes[i+1],3)
        # Negative slope diagonals
        for i in range(18):
            if i not in [4,13]:
                add_link(self.nodes[i], self.nodes[i+5], 4)
        # Positive slope diagonals
        for i in range(18):
            if i not in [0,9]:
                add_link(self.nodes[i], self.nodes[i+4], 5)