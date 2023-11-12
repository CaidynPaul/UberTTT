#counter and symbol have been used interchangably in the comments



class Board:#board class
	def __init__(self):
		self.board=[[' ',' ',' '],
					[' ',' ',' '],
					[' ',' ',' ']]
		self.board_dict={1:[0,0],2:[0,1],3:[0,2],#board values as indexes
						4:[1,0],5:[1,1],6:[1,2],#used in "convert_to_index"
						7:[2,0],8:[2,1],9:[2,2]}#function
		self.turns=0
		
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
		quit()
	
	def convert_to_index(self,user_input):#might be backend or may be kept
		return self.board_dict[user_input]#uses numerical input representing board space and returns the index version
										#gives in the form [y,x], due to array calling
	
	def add_counter(self,player_counter,xcoord,ycoord):#adds counter
		if self.board[ycoord][xcoord] == ' ':#if spot is free
			self.board[ycoord][xcoord]=player_counter
			self.turns+=1
		else:#
			pass

	
	def check_for_win(self,counter):#counter being the symbol we are checking for
		#just alot of if/elif statments to check all possible win conditions for a specific counter
		if self.board[0][0]==counter and self.board[0][1]==counter and self.board[0][2]==counter:#horizontal
			return True
		elif self.board[1][0]==counter and self.board[1][1]==counter and self.board[1][2]==counter:#horizontal
			return True
		elif self.board[2][0]==counter and self.board[2][1]==counter and self.board[2][2]==counter:#horizontal
			return True	
		elif self.board[0][0]==counter and self.board[1][1]==counter and self.board[2][2]==counter:#diagonal
			return True
		elif self.board[0][2]==counter and self.board[1][1]==counter and self.board[2][0]==counter:#diagonal
			return True	
		elif self.board[0][0]==counter and self.board[1][0]==counter and self.board[2][0]==counter:#vertical
			return True
		elif self.board[0][1]==counter and self.board[1][1]==counter and self.board[2][1]==counter:#vertical
			return True	
		elif self.board[0][2]==counter and self.board[1][2]==counter and self.board[2][2]==counter:#vertical
			return True
	
	def check_for_draw(self):
		num_of_spaces_taken=0
		for i in self.board:
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
# player1=Player('o','player1')
# player2=Player('x','player2')
# game=Board()
# turnDict = {0:"o",1:"x"}


# while True:
# 	turn=0
# 	game.display_board()
# 	print('Player 1 where would you like to go?')
# 	place=int(input('---->'))
# 	game.add_counter(turnDict[turn],game.convert_to_index(place)[1],game.convert_to_index(place)[0])
# 	if game.check_for_win(turnDict[turn]):
# 		game.win(turnDict[turn])
# 		game.display_board()

# 	if game.check_for_draw():
# 		print('DRAW')
# 		game.display_board()
# 		quit()

# 	turn=1
# 	game.display_board()
# 	print('Player 2 where would you like to go?')
# 	place=int(input('---->'))
# 	game.add_counter(turnDict[turn],game.convert_to_index(place)[1],game.convert_to_index(place)[0])
# 	game.check_for_win(turnDict[turn])
# 	if game.check_for_win(turnDict[turn]):
# 		game.win(turnDict[turn])
# 		game.display_board()
# 	if game.check_for_draw():
# 		print('DRAW')
# 		game.display_board()
# 		quit()
		

# 	#123547698
