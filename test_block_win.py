import game
import players 

if __name__ == "__main__":
    game_board = game.make_board()
    select_board = 5 #arbitrary number of the board, this AI doesn't implement this feature. 

    #empty board test
    sub1 = [
            1, 2, 3,
            4, 5, 6, 
            7, 8, 9
    ]
    m1 = 0 
    #x wins and o blocks horizontally
    sub2 = [
            'x', 2, 'x',
            4, 'o', 6, 
            7, 8, 'o'
    ]
    m2 = 2
    #x wins and o blocks vertically
    sub3 = [
            'x', 2, 3,
             4, 5, 'x', 
            'x', 'o', 'o'
    ]
    m3 = 4
    #x wins and o blocks main diagonal
    sub4 = [
            1, 2, 3,
             4, 'x', 'o', 
            'o', 'o', 'x'
    ]
    m4 = 1
    #x wins and o blocks other diagonal
    sub5 = [
            1, 2, 'x',
             'o', 5, 6, 
            'x', 'o', 'o'
    ]
    m5 = 5
    #x blocks and o wins horizontally
    sub6 = [
            1, 2, 3,
            'o', 'o', 6, 
            7, 'x', 9
    ]
    m6 = 6
    #x blocks and o wins vertically 
    sub7 = [
            1, 'o', 3,
            'x', 'o', 'x', 
            7, 8, 9
    ]
    m7 = 8
    #x blocks and o wins main diagonal
    sub8 = [
            'o', 2, 3,
            'x', 'o', 6, 
            7, 'x', 9
    ]
    m8 = 9
    #x blocks and o wins other diagonal
    sub9 = [
            1, 2, 'o',
            'x', 'o', 'x', 
            7, 8, 9
    ]
    m9 = 7
    # x wins and o blocks last horizontal
    sub10 = [
            1, 'o', 3,
            4, 'o', 6, 
            7, 'x', 'x'
    ]
    m10 = 7
    # x blocks and o wins last vertical
    sub11 = [
            'x', 'x', 3,
            4, 5, 'o', 
            7, 8, 'o'
    ]
    m11 = 3
    testWB = players.MakeWinningMoveAndBlock(1) 
    testBW = players.MakeWinningMoveAndBlock(2)
    subs = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10, sub11]
    m = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11]
    xfail = 0
    ofail = 0
    rand_move = set()
    rand_move2 = set()
    for i in range(len(subs)): 
        sub_board = subs[i]
        test_move = m[i]
        for j in range(10):
            x_player_move = testWB.make_move(sub_board, game_board, select_board)
            o_player_move = testBW.make_move(sub_board, game_board, select_board)
            if i == 0: 
                rand_move.add(x_player_move)
                rand_move2.add(o_player_move)
            else: 
                if m[i] != x_player_move:
                    message = f"Player x made a wrong move, failed case {i+1}, chose {x_player_move} instead of {m[i]}"
                    xfail += 1
                    print(message)
                    print(sub_board)
                if m[i] != o_player_move:
                    message = f"Player o made a wrong move, failed case {i+1}, chose {o_player_move} instead of {m[i]}"
                    ofail += 1
                    print(message)
                    print(sub_board)
    if xfail + ofail == 0: 
        print("All test cases passed")
    else: 
        print(f"Failed {xfail+ofail} test cases.")

            
