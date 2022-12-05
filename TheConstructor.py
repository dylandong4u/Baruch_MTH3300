class TTTBoard:

	_board = [['', '', ''],
		  ['', '', ''],
		  ['', '', '']]

	def __init__(self):
		for idx_row in range(len(self._board)):
			for idx_token in range(len(self._board[idx_row])):
				if self._board[idx_row][idx_token] == '':
					self._board[idx_row][idx_token] = ' '


# I did this because when I initiate the constructor like this:

'''
class TTTBoard:
	
	def __init__(self):
		self._board = [[' ', ' ', ' '],
			       [' ', ' ', ' '],
			       [' ', ' ', ' ']]
'''
# then I use win_for() method 

'''
def win_for(self, char):
	win = False
	
	if TTTBoard().diag_full(char):
		win = True
	
	else:
		for row_col in range(3):
			if TTTBoard().col_full(row_col, char):
				win = True
			elif TTTBoard().row_full(row_col, char):
				win = True
	
	return win
'''
# self._board is always an empty 3x3 list
