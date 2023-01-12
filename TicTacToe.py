from Board import Board, board_inst as board
from Game import Game
import os

game = Game()

while True: 
    os.system('clear')
    print("""Menu:
    
    1) New Game
    2) Exit
    """)

    choice = input("Please Select > ")
    if choice == '1': 
        game.play_game()
    elif choice == '2': 
        break
    else: 
        print("Unknown Option Selected!")

# board.print_board()
# game.make_move(0, 0, 'o')
# board.print_board()
# game.make_move(6, 5, 'x')
# board.print_board()
# game.make_move(2, 1, 'x')
# board.print_board()
# game.make_move(3, 2, 'x')
# board.print_board()
# game.make_move(4, 3, 'x')
# board.print_board()
# game.make_move(5, 4, 'x')
# board.print_board()
# print(board.get_current_state())