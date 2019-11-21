import board_util
import dice
import util

def game_loop( starting_player ):
    board = board_util.new_board()
    board_util.draw_board( board )
    game_over = False
    next_player = starting_player
    while not game_over:
        roll = dice.roll()
        move = util.ask_move( next_player, roll )
        util.move( board, move )
        board_util.draw_board( board )
        next_player = board_util.opponent( next_player )
        if board_util.game_over():
            game_over = True
