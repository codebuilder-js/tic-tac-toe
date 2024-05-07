board = {'topL': ' ', 'topM': ' ', 'topR': ' ',
         'midL': ' ', 'midM': ' ', 'midR': ' ',
         'lowL': ' ', 'lowM': ' ', 'lowR': ' '}

def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

turn = 'X'

for i in range(9):
    printBoard(board)

    move = input('Turn for ' + turn + '. Choose a space to move: ')

    board[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(board)