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
        "out": [0, 0]
    }

def number_of_pieces( board, point ):
    return board["points_number"][point]

def colour( board, point ):
    return board["points_colour"][point]

def game_over( board ):
    return ( board["out"][0] == 15 ) or ( board["out"][1] == 15 )
