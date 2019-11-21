## Represent the opponents (and their checkers etc.) with
## numbers, because we represent everything with numbers.
RED = 0
BLACK = 1

## We have to decide in which direction each opponent will proceed.
RED_HOME = 0

## The bar, where "captured" checkers are waiting.
bar = [0, 0]

## The board, initial setup:
points_number = [2, 0, 0, 0, 0, 5,
                 0, 3, 0, 0, 0, 5,
                 5, 0, 0, 0, 3, 0,
                 5, 0, 0, 0, 0, 2]
points_colour = [BLACK, 0, 0, 0, 0, RED,
                 0, RED, 0, 0, 0, BLACK,
                 RED, 0, 0, 0, BLACK, 0,
                 BLACK, 0, 0, 0, 0, RED]

## Strings for drawing the board:
colours = ["", ""]
colours[RED] = "R"
colours[BLACK] = "B"

