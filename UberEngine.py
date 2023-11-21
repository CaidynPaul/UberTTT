#counter and symbol have been used interchangably in the comments


#counter and symbol have been used interchangably in the comments

import random

class Board:#board class
	def __init__(self):
		self.board=[[' ',' ',' '],
					[' ',' ',' '],
					[' ',' ',' ']]
		self.board_dict={1:[0,0],2:[0,1],3:[0,2],#board values as indexes
						4:[1,0],5:[1,1],6:[1,2],#used in "convert_to_index"
						7:[2,0],8:[2,1],9:[2,2]}#function
		
		self.turnDict = {
			0:'o',
			1:'x'
		}
		self.turns=0
		self.winner=None

	def set_winner(self, winner):
		self.winner=winner
	def get_winner(self):
		return self.winner
	
	def get_board(self):
		return self.board
	
	def display_board(self):
		for i in self.board:
			print(i)
			
	def win(self,counter):#backend testing
		if counter=='o':
			winner='Player 1'
		else:
			winner='Player 2'
		print('You win',winner,'You were playing as',counter)
		self.winner=winner
		quit()
	
	def get_turn(self):
		return self.turnDict[self.turns]
	
		
	def convert_to_index(self,user_input):#might be backend or may be kept
		return self.board_dict[user_input]#uses numerical input representing board space and returns the index version
										#gives in the form [y,x], due to array calling
	
	def add_counter(self,xcoord,ycoord):#adds counter
		player_counter = self.turnDict[self.turns]
		if self.board[ycoord][xcoord] == ' ':#if spot is free
			self.board[ycoord][xcoord]=player_counter
		else:
			pass
		self.turns=1-self.turns

	
	def check_for_win(self,counter,board):#counter being the symbol we are checking for
		#just alot of if/elif statments to check all possible win conditions for a specific counter
		if board[0][0]==counter and board[0][1]==counter and board[0][2]==counter:#horizontal
			return True
		elif board[1][0]==counter and board[1][1]==counter and board[1][2]==counter:#horizontal
			return True
		elif board[2][0]==counter and board[2][1]==counter and board[2][2]==counter:#horizontal
			return True	
		elif board[0][0]==counter and board[1][1]==counter and board[2][2]==counter:#diagonal
			return True
		elif board[0][2]==counter and board[1][1]==counter and board[2][0]==counter:#diagonal
			return True	
		elif board[0][0]==counter and board[1][0]==counter and board[2][0]==counter:#vertical
			return True
		elif board[0][1]==counter and board[1][1]==counter and board[2][1]==counter:#vertical
			return True	
		elif board[0][2]==counter and board[1][2]==counter and board[2][2]==counter:#vertical
			return True


	def check_for_draw(self,board):
		num_of_spaces_taken=0
		for i in board:
			for j in i:
				if j==' ':
					num_of_spaces_taken+=1
		if num_of_spaces_taken==0:
			if not self.check_for_win('x',self.board) and not self.check_for_win('o',self.board):
				return True
	
	def computer_ai(self, board, comp_turn):
		state = self.evaluate(board)

		if state == 1:
			return state
		if state == -1:
			return state
		if self.check_for_draw(board):
			return 0

		if comp_turn:
			best = -2000  # basically neg infite
			for i in range(3):
				for j in range(3):
					if board[i][j] == ' ':
						board[i][j] = 'o'
						best = max([best, self.computer_ai([row[:] for row in board], not comp_turn)])
						board[i][j] = ' '  # reset change
			return best
		else:  # player/minimizer's turn
			best = 2000  # basically infite
			for i in range(3):
				for j in range(3):
					if board[i][j] == ' ':
						board[i][j] = 'x'
						best = min(best, self.computer_ai([row[:] for row in board], not comp_turn))
						board[i][j] = ' '  # reset change
			return best
	
	def find_best_move(self, board):

		bestmove = [None, None]
		bestval = -2  # starting point

		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					board[i][j] = 'o'
					move = self.computer_ai(board, False)  # evaluates move
					board[i][j] = ' '  # reset changes
					if bestval < move:
						bestmove = [i, j]
						bestval = move

		return bestmove  # i y
		
	
	def random_move(self):
		starters=[1,3,7,9]
		return random.choice(starters)
						

# oboard.add_counter(oboard.find_best_move(oboard.get_board)[0],oboard.find_best_move(oboard.get_board)[1])


	def evaluate(self,board):#ai function
		if self.check_for_win('x',board):
			return -1#comp loss
		elif self.check_for_win('o',board):
			return 1#comp win
		return 0#if draw or on winner
	
class Player:#holds the player symbol only
	def __init__(self,symbol,name):
		self.symbol=symbol
		self.name=name#just for back end


# # #concept driver code
# player1=Player('o','computer')
# player2=Player('x','player2')
# computer=True
# game=Board()
# turnDict= {0:'o',1:'x'}

# while True:
#     game.display_board()
#     place = game.find_best_move(game.board)
#     game.add_counter(place[1], place[0])
#     if game.check_for_win('o', game.board):
#         game.display_board()
#         quit()
#     if game.check_for_draw(game.board):
#         print('draw')
#         game.display_board()
#         quit()

#     game.display_board()
#     place = int(input('->'))
#     place = game.convert_to_index(place)
#     game.add_counter(place[1], place[0])
#     if game.check_for_win('x', game.board):  # Check for 'x' win
#         game.display_board()
#         quit()
#     if game.check_for_draw(game.board):
#         print('draw')
#         game.display_board()
#         quit()
