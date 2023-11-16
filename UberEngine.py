#counter and symbol have been used interchangably in the comments


#counter and symbol have been used interchangably in the comments



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
	
		
	def convert_to_index(self,user_input):#might be backend or may be kept
		return self.board_dict[user_input]#uses numerical input representing board space and returns the index version
										#gives in the form [y,x], due to array calling
	
	def add_counter(self,xcoord,ycoord,update):#adds counter
		player_counter = self.turnDict[self.turns]
		if self.board[ycoord][xcoord] == ' ':#if spot is free
			self.board[ycoord][xcoord]=player_counter
			if update:
				self.turns=1-self.turns
		else:#
			pass

	
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

	def find_win(self,counter):#counter being the symbol we are checking for.!!!!!isntaed of check_for_win we return the win type
		#just alot of if/elif statments to check all possible win conditions for a specific counter
		if self.board[0][0]==counter and self.board[0][1]==counter and self.board[0][2]==counter:#horizontal
			return 'h1'
		elif self.board[1][0]==counter and self.board[1][1]==counter and self.board[1][2]==counter:#horizontal
			return 'h2'
		elif self.board[2][0]==counter and self.board[2][1]==counter and self.board[2][2]==counter:#horizontal
			return 'h3'	
		elif self.board[0][0]==counter and self.board[1][1]==counter and self.board[2][2]==counter:#diagonal
			return 'nd'
		elif self.board[0][2]==counter and self.board[1][1]==counter and self.board[2][0]==counter:#diagonal
			return 'pd'	
		elif self.board[0][0]==counter and self.board[1][0]==counter and self.board[2][0]==counter:#vertical
			return 'v1'
		elif self.board[0][1]==counter and self.board[1][1]==counter and self.board[2][1]==counter:#vertical
			return 'v2'	
		elif self.board[0][2]==counter and self.board[1][2]==counter and self.board[2][2]==counter:#vertical
			return 'v3'
	
	def check_for_draw(self,board):
		num_of_spaces_taken=0
		for i in board:
			for j in i:
				if j==' ':
					num_of_spaces_taken+=1
		if num_of_spaces_taken==0:
			if not self.check_for_win('x') and not self.check_for_win('o'):
				return True
				


		
	
	def computer_ai(self):#using the minimax algorythm
		pass
			
	

class Player:#holds the player symbol only
	def __init__(self,symbol,name):
		self.symbol=symbol
		self.name=name#just for back end


# #concept driver code
player1=Player('o','player1')
player2=Player('x','player2')
game=Board()
turnDict = {0:"o",1:"x"}


while True:
	turn=0
	game.display_board()
	1
	
	print('Player 1 where would you like to go?')
	place=int(input('---->'))
	
	game.add_counter(game.convert_to_index(place)[1],game.convert_to_index(place)[0],True)
	if game.check_for_win(turnDict[turn],game.board):
		game.win(turnDict[turn])
		win_type=game.find_win(turnDict[turn])
		game.display_board()

	if game.check_for_draw(game.board):
		print('DRAW')
		game.display_board()
		quit()

	turn=1
	game.display_board()
	print('Player 2 where would you like to go?')
	place=int(input('---->'))
	game.add_counter(game.convert_to_index(place)[1],game.convert_to_index(place)[0],True)
	game.check_for_win(turnDict[turn],game.board)
	if game.check_for_win(turnDict[turn],game.board):
		game.win(turnDict[turn])
		win_type=game.find_win(turnDict[turn])
		game.display_board()
	if game.check_for_draw(game.board):
		print('DRAW')
		game.display_board()
		quit()
		

# 	#123547698
		

# 	#123547698
