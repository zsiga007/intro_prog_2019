## Represent the opponents (and their checkers etc.) with
## numbers, because we represent everything with numbers.
RED = 0
BLACK = 1

## We have to decide in which direction each opponent will proceed.
RED_HOME = 0

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

## Strings for drawing the board:
colours = ["", ""]
colours[RED] = "R"
colours[BLACK] = "B"

## missing: procedure draw_board( board )

## missing: ask_player_and_move( board, next_player, die1, die2 )


################
## Board printing
################
## The printed representation of each point will occupy
## three characters.  The first and the last character
## will be a space (" ") if the point contains no checker
## at all.  Otherwise, the third character will be the
## character representing the colour of the checkers at
## the point.  The first character will be non-space only
## if the point contains more than 9 checkers.

def print_point( checkers, colour_string ):
    if checkers == 0:
        print( " 0 ", end="" )
    elif checkers < 10:         # one-digit number
        ## add extra space before:
        print( " ", checkers, colour_string, sep="", end="" )
    else:                       # two-digit number
        print( checkers, colour_string, sep="", end="" )

## This procedure prints the board
## (missing: the bar is not printed).
## The board is represented by twelve consecutive
## lines, containing two points each (so we
## rotate the usual view of the board by 90 degrees).

def draw_board( points_number, points_colour ):
    ## Number of spaces between the two columns
    ## ("column separator"):
    column_sep = "        "
    ## We will print 12 lines, with two points each:
    for i in range( 12 ):
        ## Number of checkers at the two points
        ## in this row:
        checkers1 = points_number[11 - i]
        checkers2 = points_number[12 + i]
        print_point( checkers1, colours[points_colour[11 - i]] )
        print( column_sep, end="" )
        print_point( checkers2, colours[points_colour[12 + i]] )
        ## Don't forget the newline at the end of each line:
        print()

## Print board:
draw_board( points_number, points_colour )
