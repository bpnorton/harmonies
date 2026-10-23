"""
Testing!
"""

import hex
import terrain_token as tt

def test_terrain_token():
    passed = True
    node = hex.Hex("1", (0,0))
    water_token = tt.TerrainToken(0)
    wood_token1 = tt.TerrainToken(3)
    node.add_token(water_token)
    # Test basic functionality adding tokens
    if node.tokens != [water_token]:
        print("FAILED TERRAIN TOKEN TEST 1: Place token on empty hex")
        passed = False
    # Test stacking a token on top of an invalid token
    if node.add_token(wood_token1):
        print("FAILED TERRAIN TOKEN TEST 2: Place token on invalid token")
        passed = False
    # Test removing tokens
    if node.remove_token(False) == water_token:
        print("FAILED TERRAIN TOKEN TEST 4: Remove token not placed this turn")
        passed = False
    if node.remove_token(True) != water_token and node.tokens != []:
        print("FAILED TERRAIN TOKEN TEST 5: Remove token placed this turn")
        passed = False
    # Test valid stacking
    wood_token2 = tt.TerrainToken(3)
    node.add_token(wood_token1)
    node.add_token(wood_token2)
    if node.tokens != [wood_token1, wood_token2]:
        print("FAILED TERRAIN TOKEN TEST 6: Place token on valid token")
        passed = False
    # Test stacking past individual terrain type height limit
    wood_token3 = tt.TerrainToken(3)
    node.add_token(wood_token3)
    if node.tokens != [wood_token1, wood_token2]:
        print("FAILED TERRAIN TOKEN TEST 7: Stack token past terrain type height limit")
        passed = False

    return passed

def test_hex():
    passed = True

    node1 = hex.Hex("1", (0,0))
    node2 = hex.Hex("2", (1,0))
    if node1.neighbors != [None,None,None,None,None,None]:
        print("FAILED TERRAIN TOKEN TEST 1: Initialize empty neighbor list")
        passed = False
    node1.add_neighbor(node2, 0)
    node2.add_neighbor(node1, 3)
    # Test adding neighbors
    if node1.neighbors[0] != node2:
        print("FAILED GAME BOARD NODE TEST 2: Add neighbor")
        passed = False

    return passed

def test_game_state():
    passed = True

    node1 = hex.Hex("1", (0,0))
    



if __name__ == "__main__":
    passed = True

    if test_terrain_token():
        print("PASSED TERRAIN TOKEN TESTS")
    else:
        passed = False

    if test_hex():
        print("PASSED GAME BOARD NODE TESTS")
    else:
        passed = False

    if passed:
        print("PASSED ALL TESTS!")