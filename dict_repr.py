RED = 0
BLACK = 1
RED_HOME = 0

def opponent( player ):
    return ( player + 1 ) % 2

def new_board():
    return {
        "points_number": [2, 0, 0, 0, 0, 5,
                          0, 3, 0, 0, 0, 5,
                          5, 0, 0, 0, 3, 0,
                          5, 0, 0, 0, 0, 2],
        "points_colour": [BLACK, 0, 0, 0, 0, RED,
                          0, RED, 0, 0, 0, BLACK,
                          RED, 0, 0, 0, BLACK, 0,
                          BLACK, 0, 0, 0, 0, RED],
        "bar": [0, 0],
        "out": [0, 0],
        ## We can even hold 15 element lists by players,
        ## with -1 representing the bar, and 24 representing
        ## beared off:
        "black_points": [0, 0, 11, 11, 11, 11, 11,
                         16, 16, 16, 18, 18, 18, 18, 18],
        "red_points": [23, 23, 12, 12, 12, 12, 12,
                       7, 7, 7, 5, 5, 5, 5, 5],
    }

def number_of_pieces( board, point ):
    return board["points_number"][point]

def colour( board, point ):
    return board["points_colour"][point]

def game_over( board ):
    return ( board["out"][0] == 15 ) or ( board["out"][1] == 15 )
