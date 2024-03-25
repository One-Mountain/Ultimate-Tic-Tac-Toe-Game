from game import win_state, draw_state 

if __name__ == '__main__':
    #no one is winning yet, nothing happens here
    empty_state = [i for i in range(1, 10)]
    empty_winx = False
    empty_wino = False
    empty_tie = False 

    #x player wins with diagonal
    test1 = empty_state[:]
    test1[0], test1[4], test1[8] = 'x', 'x', 'x'
    test1[1], test1[7] = 'o', 'o'
    test1_winx = True 
    test1_wino = False
    test1_tie = False

    #o player wins with column 
    test2 = empty_state[:]
    test2[2], test2[5], test2[8] = 'o', 'o', 'o'
    test2[4], test2[1], test2[6] = 'x', 'x', 'x'
    test2_winx = False 
    test2_wino = True 
    test2_tie = False 

    #tie
    test3 = ['o', 'x', 'x',
             'x', 'o', 'o',
             'x', 'o', 'x']
    test3_winx = False 
    test3_wino = False 
    test3_tie = True

    #x wins with a row: 
    test4 = empty_state[:]
    test4[0], test4[1], test4[2] = 'x', 'x', 'x'
    test4[4], test4[5] = 'o', 'o'
    test4_winx = True 
    test4_wino = False 
    test4_tie = False 

    # another tie 
    test5 = ['o', 'x', 'o',
             'o', 'x', 'o',
             'x', 'o', 'x']
    test5_winx = False 
    test5_wino = False 
    test5_tie = True 

    # mid-game no wins no ties
    test6 = [1, 'x', 3,
             'o', 5, 'x',
             'o', 8, 9]
    test6_winx = False 
    test6_wino = False
    test6_tie = False 

    test_cases = [empty_state, test1, test2, test3, test4, test5, test6]
    x_wins = [empty_winx, test1_winx, test2_winx, test3_winx, test4_winx, test5_winx, test6_winx]
    o_wins = [empty_wino, test1_wino, test2_wino, test3_wino, test4_wino, test5_wino, test6_wino]
    ties = [empty_tie, test1_tie, test2_tie, test3_tie, test4_tie, test5_tie, test6_tie] 

    for i in range(len(test_cases)):
        board = test_cases[i]
        wx = win_state(board, 'x')
        wo = win_state(board, 'o')
        t = draw_state(board)
        c = 0
        txt = f'Test {i}'
        print(txt)
        if wx != x_wins[i]:
            txt = f'Failed test {i} on win condition x'
            print(txt)
            c += 1
        if wo != o_wins[i]:
            txt = f'Failed test {i} on win condition o' 
            print(txt)
            c += 1
        if t != ties[i]: 
            txt = f'Failed test {i} on tie condition'
            c += 1
        if c == 0: 
            txt = f'Passed test {i}!'
            print(txt)
        else: 
            print('results', wx, wo, t)
            print('actual', x_wins[i], o_wins[i], ties[i])