"""
Logical representation of game board
"""

import hex

COORDINATES = [(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),
               (-1,2),(0,2),(1,2),(2,2),(3,2),(-1,3),(0,3),(1,3),(2,3),
               (-2,4),(-1,4),(0,4),(1,4),(2,4)]


def add_link(hex1, hex2, direction):
    hex1.add_neighbor(hex2, direction%6)
    hex2.add_neighbor(hex1, (direction + 3)%6)


class GameBoard:

    def __init__(self):
        self.hexes = []
        for i in range(23):
            self.hexes.append(hex.Hex("n"+str(i), COORDINATES[i]))

        # Add edges: 0 = West, increasing clockwise until 5 = SW
        # Horizontals
        for i in range(22):
            if i not in [4,8,13,17]:
                add_link(self.hexes[i], self.hexes[i+1],3)
        # Negative slope diagonals
        for i in range(18):
            if i not in [4,13]:
                add_link(self.hexes[i], self.hexes[i+5], 4)
        # Positive slope diagonals
        for i in range(18):
            if i not in [0,9]:
                add_link(self.hexes[i], self.hexes[i+4], 5)