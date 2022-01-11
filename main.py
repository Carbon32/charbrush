# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#													        #
#			         Python Sprite Editor					#
#			          Developer: Carbon				        #
#													   	    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports: #

import pygame

# Pygame Initialization: 

pygame.init()

# Editor Variables: #

editorRunning = True

whiteColor = (255, 255, 255)
blackColor = (0, 0, 0)
redColor = (255, 0, 0)
greenColor = (0, 255, 0)
blueColor = (0, 0, 255)

rows = columns = 30

# Window: #

screenWidth = 600
screenHeight = 700

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Python Sprite Editor: ')

# Tool Bar: #

toolbarHeight = screenHeight - screenWidth

# Pixel Size: #

pixelSize = screenWidth // columns

# Grid Settings: #

drawGridLines = True

# FPS Handler: #

handleFPS = pygame.time.Clock()

# Editor Functions: #

def initGrid(rows : int, columns : int, color : tuple):
	grid = []
	for i in range(rows):
		grid.append([])
		for j in range(columns):
			grid[i].append(color)

	return grid

def drawGrid(window : pygame.Surface, grid : list):
	for i, row in enumerate(grid):
		for j, pixel in enumerate(row):
			pygame.draw.rect(window, pixel, (j * pixelSize, i * pixelSize, pixelSize, pixelSize))

	if(drawGridLines):
		for i in range(rows + 1):
			pygame.draw.line(window, blackColor, (0, i * pixelSize), (screenWidth, i * pixelSize))

		for i in range(columns + 1):
			pygame.draw.line(window, blackColor, (i * pixelSize, 0), (i * pixelSize, screenHeight - toolbarHeight))

# Editor Mechanics: #

grid = initGrid(rows, columns, whiteColor)

# Editor Loop: #

while(editorRunning):
	handleFPS.tick(60)
	window.fill(whiteColor)
	drawGrid(window, grid)
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			editorRunning = False

	pygame.display.update()
 

pygame.quit()