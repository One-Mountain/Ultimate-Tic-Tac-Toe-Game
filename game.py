from players import RandomPlayer, HumanPlayer
big_x = ["x", " ", "x",
         " ", "x", " ",
         "x", " ", "x"]

big_o = ["o", "o", "o",
         "o", " ", "o",
         "o", "o", "o"]

def make_board(): #create the game board made of 9 tic tac toe boards. 
    num = [i for i in range(1,10)]
    board = []
    for i in range(9):
        a = num[:] 
        board.append(a)
    return board


def render(board):
    b = ""
    for i in range(9):
        if i < 3: 
            j = 0
        elif i < 6:
            j = 3
        else: 
            j = 6
        if i == 3 or i == 6: 
            b += "-"*34 + "\n"
        a = str(board[j][3*(i%3):3*(i%3)+3]) + " | " + str(board[j+1][3*(i%3):3*(i%3)+3]) + " | " + str(board[j+2][3*(i%3):3*(i%3)+3]) + "\n"
        a = a.replace("'", "")
        b += a
    print(b)

def chosen_board(board, choice):
    return board[choice]

def get_mark(player):
    if player == 0: 
        return 'x'
    return 'o'
    
def valid_move(sub_board, choice):
    valid_inputs = [i for i in range(1,10)]
    if choice not in valid_inputs:
        return False
    if sub_board[choice-1] == 'x' or sub_board[choice-1] == 'o':
        return False
    return True

def valid_board(board_state, choice):
    valid_inputs= [i for i in range(1,10)]
    if choice not in valid_inputs: 
        return False
    if board_state[choice-1] != 0: 
        return False
    return True 
def win_state(sub_board, player):
    win_cond = [(0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,5,8),(2,4,6),(3,4,5),(6,7,8)]
    for i in win_cond: 
        if sub_board[i[0]] == player and sub_board[i[1]] == player and sub_board[i[2]] == player: 
            return True
    return False 
def draw_state(sub_board):
    nums = [i for i in range(10)]
    for i in sub_board: 
        if i in nums: 
            return False
    return True 
def board_selection(board, choice):
    return board[choice-1]
def get_board_selection(board_state, player):
    choose = player.make_move(board_state, game_board, selected_board)
    while not valid_board(board_state, choose):
        choose = player.make_move(board_state)
    return choose
def get_move(sub_board, selected_board):
    move = input("Make your move on the board " + str(selected_board)+ ": ")
    while not valid_move(sub_board, move): 
        move = input("choose a correct move: ")
    move = int(move)
    return move
def make_move(sub_board, mark, move):
    new_board = sub_board[:]
    new_board[move-1] = mark
    return new_board
def update_states(sub_board, mark, selected_board, board_state):
    new_board_state = board_state[:]
    new_sub_board = sub_board[:]
    if win_state(sub_board, mark):
        if mark == 'o':
            print('Player 2 wins this board')
            new_sub_board[:] = big_o 
        if mark == 'x':
            print('Player 1 wins this board')
            new_sub_board[:] = big_x
        new_board_state[selected_board-1] = mark
    elif draw_state(sub_board):
        new_board_state[selected_board - 1] = "D"
    return new_board_state, new_sub_board
def game_ending(board_state, mark):
    if win_state(board_state, mark):
        print("WINNER: ", current_player+1)
        print(board_state[:3])
        print(board_state[3:6])
        print(board_state[6:])
        return True
    if draw_state(board_state):
        print("It's a draw!")
        print(board_state[:3])
        print(board_state[3:6])
        print(board_state[6:])
        return True
    return False
def update_game_state(board_state, move, current_player): 
    if not valid_board(board_state, move): 
        selected_board = 0
    else: 
        selected_board = move
    current_player = (current_player + 1) % 2
    return int(selected_board), current_player
def update_game_board(sub_board, selected_board, game_board):
    new_game_board = game_board
    new_game_board[selected_board-1] = sub_board
    return new_game_board
if __name__ == "__main__":
    board_state = [0 for i in range(9)]
    current_player = 0
    gaming = True 
    selected_board = 0
    game_board = make_board()
    game_mark = ['x', 'o']
    human = HumanPlayer(1)
    comp_player1 = RandomPlayer(1)
    comp_player2 = RandomPlayer(2)
    players = [comp_player1, comp_player2]
    while gaming: 
        print("It's player", current_player +1, "turn")
        mark = game_mark[current_player]
        render(game_board)
        if selected_board == 0:
            selected_board = get_board_selection(board_state, players[current_player])
        sub_board = board_selection(game_board, selected_board)
        move = players[current_player].make_move(sub_board, game_board, selected_board)
        while not valid_move(sub_board, move):
            print("Make a valid move: ")
            move = players[current_player].make_move(sub_board, game_board, selected_board)
        sub_board = make_move(sub_board, mark, move)
        board_state, sub_board = update_states(sub_board, mark, selected_board, board_state)

        gaming = not game_ending(board_state, mark)
        game_board = update_game_board(sub_board, selected_board, game_board)
        selected_board, current_player = update_game_state(board_state, move, current_player)