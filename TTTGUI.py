import pygame
# import TTTEngine as Engine

pygame.init()
def gameScreenPlayer():
	SCREEN = pygame.display.set_mode((800,800))
	SCREEN_RECT  = SCREEN.get_rect()

	Title = "Playing against another player"
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

	board = [['o','o','o'],['x','x','x'],['x','x','o']]

	def display_board(board):
		for i in range(len(board)):
			for q in range(len(board[i])):
				if board[i][q] == "x":
					SCREEN.blit(iX,(iXRect.x+(64+margin)*q+offsetx,iXRect.y+(64+margin)*i+offsety))
				if board[i][q] == "o":
					SCREEN.blit(iO,(iORect.x+(64+margin)*q+offsetx,iORect.y+(64+margin)*i+offsety))
				if board[i][q] == " ":
					pass

	running = True

	while running:
		SCREEN.fill(('#1a1a1a'))
		display_board(board)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
				
		pygame.display.flip()

def gameScreenAi():
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

	board = [['o','o','o'],['x','x','x'],['x','x','o']]

	def display_board(board):
		for i in range(len(board)):
			for q in range(len(board[i])):
				if board[i][q] == "x":
					SCREEN.blit(iX,(iXRect.x+(64+margin)*q+offsetx,iXRect.y+(64+margin)*i+offsety))
				if board[i][q] == "o":
					SCREEN.blit(iO,(iORect.x+(64+margin)*q+offsetx,iORect.y+(64+margin)*i+offsety))
				if board[i][q] == " ":
					pass

	running = True

	while running:
		SCREEN.fill(('#1a1a1a'))
		display_board(board)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
				
		pygame.display.flip()


def titleChoice():
	SCREEN = pygame.display.set_mode((1280,720))
	SCREEN_RECT = SCREEN.get_rect()

	pygame.display.set_caption("UberSuper TicTacToe")
	
	running = True
	
	font = pygame.font.SysFont("Arial",32)
	player_choice_text = font.render("Play another Player",True,('#ffffff'))
	ai_choice_text = font.render("Play An AI",True,('#ffffff'))
	
	background_image = pygame.image.load("Title-Background.png")

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
						exit()
					
				if mx >= SCREEN_RECT.centerx-(256//2) and mx <= SCREEN_RECT.centerx-(256//2)+256:
					if my >= SCREEN_RECT.centery-128+100 and my <= SCREEN_RECT.centery-128+100+256:
						gameScreenAi()
						exit()
				
		pygame.draw.rect(SCREEN,('#772C1F'),[SCREEN_RECT.centerx-(256//2),SCREEN_RECT.centery-128,256,80])
		SCREEN.blit(player_choice_text,[SCREEN_RECT.centerx-110,SCREEN_RECT.centery-130+20])

		pygame.draw.rect(SCREEN,('#772C1F'),[SCREEN_RECT.centerx-(256//2),SCREEN_RECT.centery-128+100,256,80])
		SCREEN.blit(ai_choice_text,[SCREEN_RECT.centerx-55,SCREEN_RECT.centery-130+120])
		pygame.display.flip()


def titleScreen():
	SCREEN = pygame.display.set_mode((1280,720))
	SCREEN_RECT = SCREEN.get_rect()
	
	running = True
	
	play_font = pygame.font.SysFont("Arial",64)
	play_text = play_font.render("Play",True,('#ffffff'))
	
	background_image = pygame.image.load("Title-Background.png")

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
				
		pygame.draw.rect(SCREEN,('#772C1F'),[SCREEN_RECT.centerx-(256//2),SCREEN_RECT.centery-128,256,80])
		SCREEN.blit(play_text,[SCREEN_RECT.centerx-50,SCREEN_RECT.centery-130])
		pygame.display.flip()
if __name__ == '__main__':
	titleScreen()

