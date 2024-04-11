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
   
    def make_move(self, board):
        possible_moves = self.get_legal_moves(board)
        move = self.choose_move(possible_moves)
        return move 

class HumanPlayer:
    pass 
class MakeWinningMove: 
    pass 
class MakeWinningMoveAndBlock: 
    pass 
class FocusedOnCurrentBoard: 
    pass
