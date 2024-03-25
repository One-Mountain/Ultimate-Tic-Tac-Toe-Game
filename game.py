
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

def make_move(sub_board):
    a = input("input correct integer")
    while True: 
        if valid_move(sub_board, a):
            return a
        else: 
            a = input("Please choose a valid move")
def valid_move(sub_board, choice):
    valid_inputs = [i for i in range(1,10)]
    if not choice.isnumeric():
        return False
    choice = int(choice) 
    if choice not in valid_inputs:
        return False
    if sub_board[choice-1] == 'x' or sub_board[choice-1] == 'o':
        return False
    return True
def valid_board(board_state, choice):
    valid_inputs= [i for i in range(1,10)]
    if not choice.isnumeric():
        return False
    choice = int(choice) 
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
if __name__ == "__main__":
    board_state = [0 for i in range(9)]
    current_player = 0
    gaming = True 
    selected_board = 0
    game_board = make_board()
    while gaming: 
        print("It's player", current_player +1, "turn")
        if current_player == 0: 
            mark = 'x'
        else: 
            mark = 'o'
        render(game_board)
        if selected_board == 0: 
            choose = input('Choose a board to play on: ')
            while not valid_board(board_state, choose):
                choose = input('Please choose a correct board: ')
            selected_board = int(choose)
        sub_board = chosen_board(game_board, selected_board-1)
        move = input("Make your move on the board " + str(selected_board)+ ': ')
        while not valid_move(sub_board, move):
            move = input("choose a correct move: ")
        sub_board[int(move)-1] = mark
        if win_state(sub_board, mark): 
            board_state[selected_board - 1] = mark
        if  draw_state(sub_board): 
            board_state[selected_board - 1] = "D"
        if win_state(board_state, mark):
            print("WINNER: ", current_player+1)
            print(board_state)
            gaming = False
        if not valid_board(board_state, move):
            selected_board = 0 
        else: 
            selected_board = int(move)
        current_player = (current_player + 1) % 2
