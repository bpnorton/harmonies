"""
Logical representation of game board
"""

import game_board_node as gbn


def add_link(node1, node2, direction):
    node1.add_neighbor(node2, direction)
    node2.add_neighbor(node1, (direction + 3)%6)


class GameBoard:

    def __init__(self):
        self.nodes = []
        for i in range(23):
            self.nodes.append(gbn.GameBoardNode("n"+str(i)))

        # Add edges
        # Odd rows
        for i in range(0,19,9):
            for j in range(4):
                add_link(self.nodes[i+j], self.nodes[i+j+1],3)
        # Even rows
        for i in range(5,15,9):
            for j in range(3):
                add_link(self.nodes[i+j], self.nodes[i+j+1],3)
        # Negative slope diagonals
        for i in range(18):
            if i not in [4,13]:
                add_link(self.nodes[i], self.nodes[i+5], 4)
        # Positive slope diagonals
        for i in range(18):
            if i not in [0,9]:
                add_link(self.nodes[i], self.nodes[i+4], 5)

