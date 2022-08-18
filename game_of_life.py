import time

def check_neighbours(the_board, row, col):
    size_limit = len(the_board) - 1
    alive_cells = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            next_row = row + i
            next_col = col + j
            if next_row == row and next_col == col:
                continue
            if next_row < 0 or next_col < 0 or next_row > size_limit or next_col > size_limit:
                continue
            if the_board[next_row][next_col] == 1:
                alive_cells += 1
    return alive_cells


def game_rules(the_board):
    new_board = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],                                  
                 [0, 0, 0, 0, 0]]

    rows = len(the_board)
    cols = len(the_board)
    for row in range(rows):
        for col in range(cols):
            if check_neighbours(the_board, row, col) in [2, 3] and the_board[row][col] == 1:
                new_board[row][col] = 1
            elif check_neighbours(the_board, row, col) == 3 and the_board[row][col] == 0:
                new_board[row][col] = 1
            else:
                new_board[row][col] = 0
    return new_board




