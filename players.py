import random 
import game 
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
            if m != 'x' and m != 'o' and m != '0' and m != 'D':
                legal.append(i+1)
        return legal
    def choose_move(self, available_moves): 
        return random.choice(available_moves) 
   
    def make_move(self, board, game_board, selected_board):
        possible_moves = self.get_legal_moves(board)
        move = self.choose_move(possible_moves)
        if selected_board == 0: 
            print("Choosing board: " + str(move))
        else: 
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
class MakeWinningMove(RandomPlayer):
    def __init__(self, turn):
        super().__init__(self)
    def my_moves(self, board, game_board, selected): 
        mine = []
        for i, n in enumerate(board):
            if n == self.mark: 
                mine.append(i)
        return mine 
    def choose_move(self, available_moves, my_marks):
        win_cond = [(0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,5,8),(2,4,6),(3,4,5),(6,7,8)]
        if len(my_marks) >= 2: 
            for i in available_moves: 
                a = 0
                b = 1 
                while a < b and a < len(my_marks)-1:
                    tic = my_marks[a]
                    tac = my_marks[b]
                    combo = tuple(sorted((tic,tac,i-1)))
                    if combo in win_cond:
                        return i
                    b = b+1
                    if b >= len(my_marks)-1: 
                        a = a+1 
                        b = a+1  
        return random.choice(available_moves)
    def make_move(self, board, game_board, selected_board):
        possible_moves = self.get_legal_moves(board)
        my_marks = self.my_moves(board, game_board, selected_board)
        move = self.choose_move(possible_moves, my_marks)
        if selected_board == 0: 
            print("Choosing board: " + str(move))
        else: 
            print("Making move on board: " + str(selected_board) + " Chosen move: " + str(move))
        return move
class MakeWinningMoveAndBlock(MakeWinningMove):
    def __init__(self, turn):
        super().__init__(self)
    def opponent_marks(self, board, game_board, selected):
        if self.mark == 'x':
            op_mark = 'o'
        else: 
            op_mark = 'x'
        op_marks = []
        for i, n in enumerate(board): 
            if n == op_mark: 
                op_marks.append(i)
        return op_marks
    def choose_move(self, available_moves, my_marks, opponent):
        win_cond = [(0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,5,8),(2,4,6),(3,4,5),(6,7,8)]
        if len(my_marks) >= 2:
            for i in available_moves: 
                a = 0
                b = 1 
                while a < b and a < len(my_marks)-1:
                    tic = my_marks[a]
                    tac = my_marks[b]
                    combo = tuple(sorted((tic,tac,i-1)))
                    if combo in win_cond:
                        #print("Win move")
                        return i
                    b = b+1
                    if b >= len(my_marks)-1: 
                        a = a+1 
                        b = a+1
        if len(opponent) >= 2:
            for i in available_moves:
                a = 0 
                b = 1
                while a < b and a < len(opponent)-1:
                    tic = opponent[a]
                    tac = opponent[b]
                    combo = tuple(sorted((tic,tac,i-1)))
                    if combo in win_cond:
                        #print("Block move") 
                        return i
                    b = b+1
                    if b >= len(opponent): 
                        a += 1
                        b = a+1
        #print("Random Move")
        return random.choice(available_moves)
    def make_move(self, board, game_board, selected_board):
        possible_moves = self.get_legal_moves(board)
        my_marks = self.my_moves(board, game_board, selected_board)
        op_marks = self.opponent_marks(board, game_board, selected_board)
        move = self.choose_move(possible_moves, my_marks, op_marks)
        if selected_board == 0: 
            print("Choosing board: " + str(move))
        else: 
            print("Making move on board: " + str(selected_board) + " Chosen move: " + str(move))
        return move

class FocusedOnCurrentBoard(RandomPlayer):
    def __init__(self, turn):
        super().__init__(self)
        if self.turn == 1: 
            self.opponent_mark = 'o'
        else: 
            self.opponent_mark = 'x'
    def minimax_score(self, sub_board, player_turn, optimized_player):
        if player_turn == 1:
            cur_mark = 'x'
        else: 
            cur_mark = 'o'
        if optimized_player == 1: 
            opti_mark = 'x'
            oppo_mark = 'o'
        else: 
            opti_mark = 'o'
            oppo_mark = 'x'
        if game.win_state(sub_board, opti_mark):
            return 10
        elif game.win_state(sub_board, oppo_mark):
            return -10
        elif game.draw_state(sub_board):
            return 0
        legal_moves = self.get_legal_moves(sub_board)
        scores = []
        for move in legal_moves: 
            new_board = self.made_move(sub_board, cur_mark, move)
            opponent = (player_turn +1) % 2 
            score = self.minimax_score(new_board, opponent, optimized_player)
            scores.append(score)
        if player_turn == optimized_player:
            return max(scores)
        else: 
            return min(scores)
    def made_move(self, sub_board, cur_mark, move):
        new_board = sub_board[:]
        new_board[move-1] = cur_mark
        return new_board
    def minimax_play(self, sub_board, player_turn):
        best_move = None 
        best_score = None
        if player_turn == 1:
            cur_mark = 'x'
        else: 
            cur_mark = 'o' 
        for move in self.get_legal_moves(sub_board):
            new_board = self.made_move(sub_board, cur_mark, move)
            if player_turn == 1:
                opp = 0
            else: 
                opp = 1
            score = self.minimax_score(new_board, opp, player_turn)
            if best_score is None or score > best_score: 
                best_move = move 
                best_score = score
        return best_move 
    def make_move(self, board, game_board, selected_board):
        move = self.minimax_play(board, self.turn)
        if selected_board == 0: 
            print("Choosing board: " + str(move))
        else: 
            print("Making move on board: " + str(selected_board) + " Chosen move: " + str(move))
        return move