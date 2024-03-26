import random 
class random_player: 
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
   
    def make_move(self, game_board, board_state, board):
        self.update_board(game_board, board_state)
        possible_moves = self.get_legal_moves(board)
        move = self.choose_move(possible_moves)
        return move 

class human_player:
    pass 
class make_winning_move: 
    pass 
class make_winning_move_and_block: 
    pass 
class focused_on_current_board: 
    pass
