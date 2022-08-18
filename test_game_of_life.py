import game_of_life


def test_neighbours():
    theboard = [[0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]]
    assert game_of_life.neighbours(theboard, 0, 0) == 2
    assert game_of_life.neighbours(theboard, 1, 1) == 2
    assert game_of_life.neighbours(theboard, 2, 1) == 1


def test_rules():
    "Checking for rules are correctly applied"
    theboard = [[0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
    result = [[0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert game_of_life.rules(theboard) == result