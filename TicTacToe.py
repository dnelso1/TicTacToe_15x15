from Board import Board

board = Board()
board.print_board()
board.make_move(0, 0, 'o')
board.print_board()
board.make_move(6, 5, 'x')
board.print_board()
board.make_move(2, 1, 'x')
board.print_board()
board.make_move(3, 2, 'x')
board.print_board()
print(board.get_current_state())