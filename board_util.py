import dict_repr as board_repr
import vertical_draw as draw

## Represent the opponents (and their checkers etc.) with
## numbers, because we represent everything with numbers.
RED = board_repr.RED
BLACK = board_repr.BLACK

## We have to decide in which direction each opponent will proceed.
RED_HOME = board_repr.RED_HOME

def new_board():
    return board_repr.new_board()

def ask_player_and_move( board, next_player, die1, die2 ):
    ## missing:
    pass

def opponent( player ):
    return board_repr.opponent( player )

def game_over( board ):
    return board_repr.game_over( board )

def draw_board( board ):
    draw.draw_board( board )

def is_move_possible( board, player, fromPoint, toPoint ):
    """
    Checks if a given move is legitimate
    (only makes sure that there is no checker waiting on the bar
    (unless the move is from the bar), and that the target point 
    contains `player`'s checkers, no checker or exactly one of
    opponent's checkers.
    """
    if not board_repr.has_checker( player, board, fromPoint ):
        return False
    if board_repr.has_checkers_on_bar( player, board ):
        if not fromPoint == board_repr.BAR:
            return False
    
    ## temporary:
    return True

