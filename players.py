import random 
class RandomPlayer: 
    def __init__(self, turn):
        self.turn = turn
        if turn == 1: 
            self.mark = 'x'
        else: 
            self.mark = 'o'
    def get_legal_moves(self, board):
        legal = []
        for i, m in enumerate(board): 
            if m != 'x' and m != 'o':
                legal.append(i+1)
        return legal
    def choose_move(self, available_moves): 
        return random.choice(available_moves) 
   
    def make_move(self, board, game_board, selected_board):
        possible_moves = self.get_legal_moves(board)
        move = self.choose_move(possible_moves)
        print("Making move on board: " + str(selected_board) + " Chosen move: " + str(move))
        return move 

class HumanPlayer(RandomPlayer):
    def __init__(self, turn):
        super().__init__(self)
    
    def make_move(self, board, game_board, selected_board):
        if selected_board == 0: 
            choose = input('Choose a board to play on: ')
            while not choose.isnumeric():
                choose = input('Please choose a correct board: ')
            return int(choose)
        else: 
            choose = input("Make your move on the board " + str(selected_board) + ": ")
            while not choose.isnumeric():
                choose = input("Please choose a correct move: ")
            return int(choose)
class MakeWinningMove: 
    pass 
class MakeWinningMoveAndBlock: 
    pass 
class FocusedOnCurrentBoard: 
    pass
