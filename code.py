def isWin(board):
    """
    GIven a board checks if it is in a winning state.
    Arguments:
          board: a list containing X,O or -.
    Return Value:
           True if board in winning state. Else False
    """
    ### check if any of the rows has winning combination
    for i in range(3):
        if len(set(board[i*3:i*3+3])) is  1 and board[i*3] is not '-': return True,board[i*3]
    ### check if any of the Columns has winning combination
    for i in range(3):
       if (board[i] is board[i+3]) and (board[i] is  board[i+6]) and board[i] is not '-':
           return True,board[i]
    ### 2,4,6 and 0,4,8 cases
    if board[0] is board[4] and board[4] is board[8] and board[4] is not '-':
        return  True,board[4]
    if board[2] is board[4] and board[4] is board[6] and board[4] is not '-':
        return  True,board[4]
    return False,0


def nextMove(board,player):
    """
    Computes the next move for a player given the current board state and also
    computes if the player will win or not.
    Arguments:
        board: list containing X,- and O
        player: one character string 'X' or 'O'
    Return Value:
        willwin: 1 if 'X' is in winning state, 0 if the game is draw and -1 if 'O' is
                    winning
        nextmove: position where the player can play the next move so that the
                         player wins or draws or delays the loss
    """
    ### when board is '---------' evaluating next move takes some time since
    ### the tree has 9! nodes. But it is clear in that state, the result is a draw
    ### if len(set(board)) == 1: return 0,4

    nextplayer = 'X' if player=='O' else 'O'
    yy=isWin(board)
    if yy[0]:
        if player is 'X': return -1,0
        else: return 1,0
    res_list=[] # list for appending the result
    c= board.count('-')
    if  c is 0:
        return 0,0
    _list=[] # list for storing the indexes where '-' appears
    for i in range(len(board)):
        if board[i] == '-':
            _list.append(i)
    #tempboardlist=list(board)
    for i in _list:
        board[i]=player
        ret,move=nextMove(board,nextplayer)
        res_list.append(ret)
        board[i]='-'
        if player=='X' and ret==1:
            break
        if player=='O' and ret==-1:
            break
    if player is 'X':
        maxele=max(res_list)
        return maxele,_list[res_list.index(maxele)]
    else :
        minele=min(res_list)
        return minele,_list[res_list.index(minele)]


def Board_print(board):
    print("---------------")
    for i in range(3):
        print(board[i*3]," | ",board[i*3+1]," | ",board[i*3+2])
        print("---------------")


board=['-','-','-','-','-','-','-','-','-']
for i in range(9):
    Board_print(board)
    if i%2==0:
        x=int(input())
        board[x-1]='X'
    else:
        x=nextMove(board,'O')
        board[x[1]]='O'
    y=isWin(board)
    if y[0]==True:
        Board_print(board)
        print(y[1],' Wins')
        break;
if y[0]==False:
    Board_print(board)
    print("Draw")
