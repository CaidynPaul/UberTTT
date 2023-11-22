import pygame, pygame.mixer
import UberEngine as Engine

pygame.init()
pygame.mixer.init()

icon = pygame.image.load("AppIcon.png")
pygame.display.set_icon(icon)

Clock = pygame.time.Clock()
def gameScreenPlayer():
	SCREEN = pygame.display.set_mode((800,800)) # Set SCREEN SIZE and Surface
	SCREEN_RECT  = SCREEN.get_rect() # Get the Screen's Positional Values

	Title = "Playing against another player" # Set the title of the window
	pygame.display.set_caption(Title)

	iX = pygame.image.load("X.png") # load the X and O images
	iO = pygame.image.load("O.png")

	iX = pygame.transform.scale(iX,(64,64)) # and make sure they are the correct scale
	iO = pygame.transform.scale(iO,(64,64))

	iXRect = iX.get_rect() # get thier positional values
	iORect = iO.get_rect()

	margin = 20

	offsetx = SCREEN_RECT.centerx-96-margin
	offsety = SCREEN_RECT.centery-300-margin

	oboard = Engine.Board()	# Get the board Object
	
	def display_board(board): # Function to display the board to the screen
		for i in range(len(board)):
			for q in range(len(board[i])):
				if board[i][q] == "x":
									
					SCREEN.blit(iX,(iXRect.x+(64+margin)*q+offsetx,iXRect.y+(64+margin)*i+offsety))
					
				if board[i][q] == "o":
							
					SCREEN.blit(iO,(iORect.x+(64+margin)*q+offsetx,iORect.y+(64+margin)*i+offsety))
					
				if board[i][q] == " ":
					# pygame.draw.rect(SCREEN,(255,0,255),[iXRect.x+(64+margin)*q+offsetx,iXRect.y+(64+margin)*i+offsety,64,64])
					pass
		# Draw guide lines for the board
		line_width = 3

		# Draw the guide lines
		pygame.draw.line(SCREEN,('#e4e4e4'),(358,80),(358,315),line_width) # Verticle
		pygame.draw.line(SCREEN,('#e4e4e4'),(358+10+64+10,80),(358+10+64+10,315),line_width) #Verticle
		pygame.draw.line(SCREEN,('#e4e4e4'),(270,153),(530,153),line_width) # Horizontal
		pygame.draw.line(SCREEN,('#e4e4e4'),(270,153+10+64+10),(530,153+10+64+10),line_width) # Horizontal
	
	click_effect = pygame.mixer.Sound("click_effect.mp3") # load the click sound effect
	effect_channel = pygame.mixer.Channel(0) # define the audio channel
	effect_channel.set_volume(1) # set the volume to max

	
	running = True
	
	while running:# Game loop
		
		board = oboard.get_board() #get the board (2d array)
		SCREEN.fill(('#1a1a1a')) # fill the board with a solid colour (dark Gray)
		display_board(board)# display the board
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
			
			if e.type == pygame.MOUSEBUTTONDOWN: # get mouse input
				
				mx,my = pygame.mouse.get_pos() # get mouse position

				if mx >= 284 and mx <= 284+64: # add a counter to the position where the mouse was clicked
					if my >= 80 and my <= 80+64:
						oboard.add_counter(0,0)
						effect_channel.play(click_effect)
										
				if mx >= 284+64+20 and mx <= 284+64+64+20:
					if my >= 80 and my <= 80+64:
						oboard.add_counter(1,0)
						effect_channel.play(click_effect)
						
				
				if mx >= 284+64+20+64+20 and mx <= 284+64+64+20+64+20:
					if my >= 80 and my <= 80+64:
						oboard.add_counter(2,0)
						effect_channel.play(click_effect)
						
				# Second Row
				if mx >= 284 and mx <= 284+64:
					if my >= 80+64+20 and my <= 80+64+64+20:
						oboard.add_counter(0,1)
						effect_channel.play(click_effect)
						
				
				if mx >= 284+64+20 and mx <= 284+64+64+20:
					if my >= 80+64+20 and my <= 80+64+64+20:
						oboard.add_counter(1,1)
						effect_channel.play(click_effect)
						
				
				if mx >= 284+64+20+64+20 and mx <= 284+64+64+20+64+20:
					if my >= 80+64+20 and my <= 80+64+64+20:
						oboard.add_counter(2,1)
						effect_channel.play(click_effect)
						
				# Third Row
				if mx >= 284 and mx <= 284+64:
					if my >= 80+64+20+64+20 and my <= 80+64+64+20+64+20:
						oboard.add_counter(0,2)
						effect_channel.play(click_effect)
						
				
				if mx >= 284+64+20 and mx <= 284+64+64+20:
					if my >= 80+64+20+64+20 and my <= 80+64+64+20+64+20:
						oboard.add_counter(1,2)
						effect_channel.play(click_effect)
						
				
				if mx >= 284+64+20+64+20 and mx <= 284+64+64+20+64+20:
					if my >= 80+64+20+64+20 and my <= 80+64+64+20+64+20:
						oboard.add_counter(2,2)
						effect_channel.play(click_effect)
					
		if oboard.check_for_win('o',oboard.get_board()): # Check win for Player1
			winScreen("Computer")
			quit()
		if oboard.check_for_win('x',oboard.get_board()): # Check win for Player2
			winScreen("Human")
			quit()
		
		if oboard.check_for_draw(oboard.get_board()): # Check for draw
			drawScreen()
			quit()

		pygame.display.flip() # Update the display

def gameScreenAi(): # Game Screen for PVE
	SCREEN = pygame.display.set_mode((800,800))
	SCREEN_RECT  = SCREEN.get_rect()

	Title = "Playing against Engine"
	pygame.display.set_caption(Title)

	iX = pygame.image.load("X.png")
	iO = pygame.image.load("O.png")

	iX = pygame.transform.scale(iX,(64,64))
	iO = pygame.transform.scale(iO,(64,64))

	iXRect = iX.get_rect()
	iORect = iO.get_rect()

	margin = 20

	offsetx = SCREEN_RECT.centerx-96-margin
	offsety = SCREEN_RECT.centery-300-margin

	oboard = Engine.Board()

	def display_board(board):
		for i in range(len(board)):
			for q in range(len(board[i])):
				if board[i][q] == "x":
					SCREEN.blit(iX,(iXRect.x+(64+margin)*q+offsetx,iXRect.y+(64+margin)*i+offsety))
				if board[i][q] == "o":
					SCREEN.blit(iO,(iORect.x+(64+margin)*q+offsetx,iORect.y+(64+margin)*i+offsety))
				if board[i][q] == " ":
					pass
		# Draw guide lines for the board
		pygame.draw.line(SCREEN,('#e4e4e4'),(360,80),(360,315)) # Verticle
		pygame.draw.line(SCREEN,('#e4e4e4'),(360+10+64+10,80),(360+10+64+10,315)) #Verticle
		pygame.draw.line(SCREEN,('#e4e4e4'),(270,150),(530,150)) # Horizontal
		pygame.draw.line(SCREEN,('#e4e4e4'),(260,150+10+64+10),(530,150+10+64+10)) # Horizontal

	running = True

	click_effect = pygame.mixer.Sound("click_effect.mp3") # load the click sound effect
	effect_channel = pygame.mixer.Channel(0) # define the audio channel
	effect_channel.set_volume(1) # set the volume to max

	while running:
		board = oboard.get_board()
		SCREEN.fill(('#1a1a1a'))
		display_board(board)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
			
			if e.type == pygame.MOUSEBUTTONDOWN: # get mouse input
				
				mx,my = pygame.mouse.get_pos() # get mouse position
				
				if oboard.get_turn() == 'x':
					if mx >= 284 and mx <= 284+64: # add a counter to the position where the mouse was clicked
						if my >= 80 and my <= 80+64:
							oboard.add_counter(0,0)
							effect_channel.play(click_effect)
											
					if mx >= 284+64+20 and mx <= 284+64+64+20:
						if my >= 80 and my <= 80+64:
							oboard.add_counter(1,0)
							effect_channel.play(click_effect)
							
					
					if mx >= 284+64+20+64+20 and mx <= 284+64+64+20+64+20:
						if my >= 80 and my <= 80+64:
							oboard.add_counter(2,0)
							effect_channel.play(click_effect)
							
					# Second Row
					if mx >= 284 and mx <= 284+64:
						if my >= 80+64+20 and my <= 80+64+64+20:
							oboard.add_counter(0,1)
							effect_channel.play(click_effect)
							
					
					if mx >= 284+64+20 and mx <= 284+64+64+20:
						if my >= 80+64+20 and my <= 80+64+64+20:
							oboard.add_counter(1,1)
							effect_channel.play(click_effect)
							
					
					if mx >= 284+64+20+64+20 and mx <= 284+64+64+20+64+20:
						if my >= 80+64+20 and my <= 80+64+64+20:
							oboard.add_counter(2,1)
							effect_channel.play(click_effect)
							
					# Third Row
					if mx >= 284 and mx <= 284+64:
						if my >= 80+64+20+64+20 and my <= 80+64+64+20+64+20:
							oboard.add_counter(0,2)
							effect_channel.play(click_effect)
							
					
					if mx >= 284+64+20 and mx <= 284+64+64+20:
						if my >= 80+64+20+64+20 and my <= 80+64+64+20+64+20:
							oboard.add_counter(1,2)
							effect_channel.play(click_effect)
							
					
					if mx >= 284+64+20+64+20 and mx <= 284+64+64+20+64+20:
						if my >= 80+64+20+64+20 and my <= 80+64+64+20+64+20:
							oboard.add_counter(2,2)
							effect_channel.play(click_effect)

			if oboard.get_turn() == 'o':

				best_move = oboard.find_best_move(oboard.get_board())
				oboard.add_counter(best_move[1],best_move[0])
				effect_channel.play(click_effect)
			
			
			if oboard.check_for_win('o',oboard.get_board()): # Check win for Player1
				winScreen("Player 1")
				quit()
			if oboard.check_for_win('x',oboard.get_board()): # Check win for Player2
				winScreen("Player 2")
				quit()
			
			if oboard.check_for_draw(oboard.get_board()): # Check for draw
				drawScreen()
				quit()
			
				
		pygame.display.flip()

def titleChoice(): # SCREEN to choose whether to play verus AI or Human
	SCREEN = pygame.display.set_mode((1280,720))
	SCREEN_RECT = SCREEN.get_rect()

	pygame.display.set_caption("Made by Caidyn And Yusuf")
	
	running = True
	
	font = pygame.font.SysFont("Arial",32)
	player_choice_text = font.render("Play another Player",True,('#ffffff'))
	ai_choice_text = font.render("Play An AI",True,('#ffffff'))
	
	background_image = pygame.image.load("Title-Background.png")
	background_image = pygame.transform.scale(background_image,(1280,720))


	while running:
		SCREEN.blit(background_image,SCREEN_RECT)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
			
			if e.type == pygame.MOUSEBUTTONDOWN:
				mx,my = pygame.mouse.get_pos()
				if mx >= SCREEN_RECT.centerx-(256//2) and mx <= SCREEN_RECT.centerx-(256//2)+256:
					if my >= SCREEN_RECT.centery-128 and my <= SCREEN_RECT.centery-128+80:
						gameScreenPlayer()
						quit()
					
				if mx >= SCREEN_RECT.centerx-(256//2) and mx <= SCREEN_RECT.centerx-(256//2)+256:
					if my >= SCREEN_RECT.centery-128+100 and my <= SCREEN_RECT.centery-128+100+256:
						gameScreenAi()
						quit()
				
		pygame.draw.rect(SCREEN,('#421200'),[SCREEN_RECT.centerx-(256//2),SCREEN_RECT.centery-128,256,80],border_radius = 8)
		SCREEN.blit(player_choice_text,[SCREEN_RECT.centerx-110,SCREEN_RECT.centery-130+20])

		pygame.draw.rect(SCREEN,('#421200'),[SCREEN_RECT.centerx-(256//2),SCREEN_RECT.centery-128+100,256,80],border_radius = 10)
		SCREEN.blit(ai_choice_text,[SCREEN_RECT.centerx-55,SCREEN_RECT.centery-130+120])
		pygame.display.flip()

def titleScreen(): # Title Screen
	SCREEN = pygame.display.set_mode((1280,720))
	SCREEN_RECT = SCREEN.get_rect()
	
	pygame.display.set_caption("UberSuper TicTacToe")

	running = True
	
	play_font = pygame.font.SysFont("Arial",64)
	play_text = play_font.render("Play",True,('#ffffff'))
	
	background_image = pygame.image.load("Title-Background.png")
	background_image = pygame.transform.scale(background_image,(1280,720))

	while running:
		SCREEN.blit(background_image,SCREEN_RECT)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
			
			if e.type == pygame.MOUSEBUTTONDOWN:
				mx,my = pygame.mouse.get_pos()
				if mx >= SCREEN_RECT.centerx-(256//2) and mx <= SCREEN_RECT.centerx-(256//2)+256:
					if my >= SCREEN_RECT.centery-128 and my <= SCREEN_RECT.centery-128+80:
						titleChoice()
						exit()
				
		pygame.draw.rect(SCREEN,('#421200'),[SCREEN_RECT.centerx-(256//2),SCREEN_RECT.centery-128,256,80],border_radius = 7)
		SCREEN.blit(play_text,[SCREEN_RECT.centerx-50,SCREEN_RECT.centery-130])
		pygame.display.flip()

def winScreen(winner=None): # Win Screen takes in a winner argument as a string
	SCREEN = pygame.display.set_mode((1280,720))
	SCREEN_RECT = SCREEN.get_rect()

	
	win_background = pygame.image.load("win-Background.png")


	font_size = 110
	win_font = pygame.font.SysFont("Consolas",font_size)

	win_text = win_font.render(winner,True,('#fcc603'))

	home_image = pygame.image.load("Home.png")

	pygame.display.set_caption(f"Winner : {winner}")

	win_effect = pygame.mixer.Sound("win_effect.mp3")
	Effects_Channel = pygame.mixer.Channel(0)

	Effects_Channel.play(win_effect)
	running = True

	while running:
		SCREEN.blit(win_background, SCREEN_RECT)
		SCREEN.blit(win_text,(SCREEN_RECT.centerx-230,SCREEN_RECT.centery+160))
		pygame.draw.rect(SCREEN,('#4b0ebe'),[SCREEN_RECT.width-64,SCREEN_RECT.height-64,64,64])
		SCREEN.blit(home_image,(SCREEN_RECT.width-64,SCREEN_RECT.height-64))		
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
			
			if e.type == pygame.MOUSEBUTTONUP:
				mx,my = pygame.mouse.get_pos()

				if mx in range(SCREEN_RECT.width-64,SCREEN_RECT.width) and my in range(SCREEN_RECT.height-64,SCREEN_RECT.height):
					Effects_Channel.stop()
					titleScreen()
					exit()
		
		pygame.display.flip()

def drawScreen(): # Draw Screen
	SCREEN = pygame.display.set_mode((1280,720))
	SCREEN_RECT = SCREEN.get_rect()

	
	draw_background = pygame.image.load("Draw-Background.png")



	home_image = pygame.image.load("Home.png")

	pygame.display.set_caption("DRAW!")
	draw_effect = pygame.mixer.Sound("draw_effect.mp3")
	Effects_Channel = pygame.mixer.Channel(0)

	Effects_Channel.play(draw_effect)

	running = True
	while running:
		SCREEN.blit(draw_background, SCREEN_RECT)
		
		pygame.draw.rect(SCREEN,('#303030'),[SCREEN_RECT.width-64,SCREEN_RECT.height-64,64,64])
		SCREEN.blit(home_image,(SCREEN_RECT.width-64,SCREEN_RECT.height-64))		
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
			
			if e.type == pygame.MOUSEBUTTONUP:
				mx,my = pygame.mouse.get_pos()

				if mx in range(SCREEN_RECT.width-64,SCREEN_RECT.width) and my in range(SCREEN_RECT.height-64,SCREEN_RECT.height):
					Effects_Channel.stop()
					titleScreen()
					exit()
		
		pygame.display.flip()

def introScreen(): # Intro Screen with Tic Tac Toe reveal animation
	SCREEN = pygame.display.set_mode((1280, 720))
	SCREEN_RECT = SCREEN.get_rect()

	pygame.display.set_caption("UberSuper TicTacToe")

	running = True
	animation_complete = False  # New variable to track animation completion

	font_title = pygame.font.SysFont("Calibri", 200)
	font_subtitle = pygame.font.SysFont("Calibri", 50)

	color1 = pygame.Color('#000000')
	color2 = pygame.Color('#CFB53B')

	text_title = font_title.render("Tic Tac Toe", True, color1)
	text_subtitle = font_subtitle.render("Made by: Caidyn Paul & Yusuf Sajjad", True, color2)

	transition_duration = 5000  # in milliseconds
	start_time = pygame.time.get_ticks()

	POP_effect = pygame.mixer.Sound("intro_effect.mp3")
	Effects_Channel = pygame.mixer.Channel(0)
	Effects_Channel.set_volume(1)

	while running:
		elapsed_time = pygame.time.get_ticks() - start_time

		if elapsed_time < transition_duration:
			# Calculate the intermediate color
			progress = elapsed_time / transition_duration
			intermediate_color = pygame.Color(
				int(color1.r + progress * (color2.r - color1.r)),
				int(color1.g + progress * (color2.g - color1.g)),
				int(color1.b + progress * (color2.b - color1.b))
			)
			text_title = font_title.render("Tic Tac Toe", True, intermediate_color)
		else:
			animation_complete = True  # Set animation completion status

		SCREEN.blit(text_title, (SCREEN_RECT.centerx - (text_title.get_width() / 2), SCREEN_RECT.centery - 80))

		if animation_complete:
			# Display the subtitle after the animation is complete
			Effects_Channel.play(POP_effect)
			SCREEN.blit(text_subtitle, (SCREEN_RECT.centerx - (text_subtitle.get_width() / 2), SCREEN_RECT.centery + 100))


		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False

		pygame.display.flip()

		if animation_complete:
			# Perform actions after the animation is complete
			# For now, we'll just exit the loop after the animation
			pygame.time.wait(3000)

			titleScreen()
			quit()

if __name__ == '__main__': # automatically run the app when the file is opened
	introScreen()
