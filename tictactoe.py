#******************************************************************************
# tictactoe.py
#******************************************************************************
# Name: Kun Dong 
#******************************************************************************
# Overall notes (not to replace inline comments):
#
# Collab: https://stackoverflow.com/questions/21598872/how-to-create-multiple-class-objects-with-a-loop-in-python - line 174
# 

class TTTBoard:
    
    _board = [['', '', ''],
              ['', '', ''],
              ['', '', '']]
    
    def __init__(self):

        for idx_row in range(len(self._board)):
            for idx_token in range(len(self._board[idx_row])):
                if self._board[idx_row][idx_token] == '':
                    self._board[idx_row][idx_token] = ' '
                
    '''
    def __init__(self):
        self._board = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]
    '''
    def display(self):
        for row in self._board:
            
            for token in row:
                print(token, end = ' ')

            print()


    def set(self, row, col, char):
        
        self._board[row][col] = char


    def occupied(self, row, col):
        
        if self._board[row][col] == 'x' or self._board[row][col] == 'o':
            return True
        
        elif self._board[row][col] == ' ':
            return False


    def row_full(self, row, char):
        cond = True
        for token in self._board[row]:
            if token != char:
                cond = False

        return cond

    def col_full(self, col, char):
        cond = True
        for row in [0,1,2]:
            if self._board[row][col] != char:
                cond = False
        return cond

    def diag_full(self, char): 
        lef_rig = (self._board[0][0] == char and self._board[1][1] == char and self._board[2][2] == char)
        rig_lef = (self._board[0][2] == char and self._board[1][1] == char and self._board[2][0] == char)

        return rig_lef or lef_rig

    def win_for(self, char):
        '''
        print(char)
        TTTBoard().display()
        print("********")
        print(self._board)
        '''
        win = False
        
        '''But TTTBoard() always returns an empty 3x3 list, different from self._board()'''
        '''The methods should be used on class object right?'''
        if TTTBoard().diag_full(char):
            win = True
            
        else:
            for row_col in range(3):
                if TTTBoard().col_full(row_col, char):
                    win = True
                elif TTTBoard().row_full(row_col, char):
                    win = True
        
        return win


    
    def random_move(self, char):

        import random

        sucess = False

        while not sucess:

            rand_row = random.randrange(0,3)
            rand_col = random.randrange(0,3)

            occupied = TTTBoard().occupied(rand_row, rand_col) # if a random location is occupied, true; unoccupied, false

            if not occupied: 
                self._board[rand_row][rand_col] = char
                sucess = True
                print('sucess + 1', sucess)
            print('its running', rand_row, rand_col)
    





def main():
    ############################################################################
    # TEST CODE: DO NOT REMOVE IN FINAL SUBMISSION!
    ############################################################################
    myGame = TTTBoard()
    myGame.display()

    # Only run the following lines after you've written .set()
    # This should print something that looks kind of like
    # x o x
    # o x
    # x

    myGame.set(0, 0, 'x')
    myGame.set(0, 1, 'o')
    myGame.set(0, 2, 'x')
    myGame.set(1, 0, 'o')
    myGame.set(1, 1, 'x')
    myGame.set(2, 0, 'x')
    myGame.display()

    # Only run the following lines after you've written .occupied()
    # This should print out
    # True True True
    # True True False
    # True False False

    print(myGame.occupied(0,0),myGame.occupied(0,1),myGame.occupied(0,2))
    print(myGame.occupied(1,0),myGame.occupied(1,1),myGame.occupied(1,2))
    print(myGame.occupied(2,0),myGame.occupied(2,1),myGame.occupied(2,2))
    
    
    # Only run the following lines after you've written .win_for()
    # This should print out:
    # True
    # False
    
    print(myGame.win_for('x'))
    print(myGame.win_for('o'))

    # Only run the following lines after you've written .random_move()
    myGame.random_move('x')
    myGame.display()
    myGame.random_move('o')
    myGame.display()


    ############################################################################
    # END OF TEST CODE.
    # PLACE YOUR SIMULATION CODE BELOW.
    ############################################################################


# main()


Trials = 3
x_won = 0

objs = [TTTBoard() for i in range(Trials)] # objs is a list that includes entries of class objects


emt = []
for i in range(Trials):
    emt.append(TTTBoard())
print(emt)

for entry in objs:
    print(entry)
    winner = None
    for move in range(4):
        entry.random_move('x')
        entry.random_move('o')
           
        

    if entry.win_for('x'):
        winner = 'x'
        x_won += 1
        print('worked')

    elif entry.win_for('o'):
        winner = 'o'
        print('o worked')

    print('after 8 moves')
    entry.display()  

    entry.random_move('x')
    print('after completion')
    entry.display()

    if winner == None:
        if entry.win_for('x'):
            winner = 'x'
            x_won += 1
        elif entry.win_for('o'):
            winner = 'o'
    print("Done here")
    
    #break

print(winner)
print(x_won/Trials)
print(emt)
print(objs[0]._board, objs[1]._board, objs[2]._board)


# Why my looping through the list to create class objects doesn't work??????