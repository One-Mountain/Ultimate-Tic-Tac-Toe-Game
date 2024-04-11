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
                    combo = (tic, tac,i-1)
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
                    combo = (tic,tac,i-1)
                    if combo in win_cond:
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
                    combo = (tic, tac, i-1)
                    if combo in win_cond: 
                        return i
                    b = b+1
                    if b >= len(opponent) -1: 
                        a += 1
                        b = a+1
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

class FocusedOnCurrentBoard: 
    pass
