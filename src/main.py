import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

def msgSurface(text):
	smallText = pygame.font.Font('freesansbold.ttf', 20)
	largeText = pygame.font.Font('freesansbold.ttf', 150)

	titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
	titleTextRect.center = surfaceWidth/2, surfaceHeight/2
	surface.blit(titleTextSurf, titleTextRect)

	typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
	titleTextRect.center = surfaceWidth/2, ((surfaceHeight/2) + 100)
	surface.blit(typTextSurf, typTextRect)

	pygame.display.update()
	time.sleep(1)


def gameOver():
	msgSurface('Kaboom!')

def helicopter(x, y, image):
	surface.blit(img, (x,y))

img = pygame.image.load('../img/bee.png')
img = pygame.transform.scale(img, (55, 50))

x = 150
y = 200

y_move = 5

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_move = -5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				y_move = 5

	y += y_move

	surface.fill(black)
	helicopter(x, y, img)

	if y > surfaceHeight-50 or y < 0:
		gameOver()

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()