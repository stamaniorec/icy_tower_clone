import pygame
pygame.init()

class Platform:
	color = (255, 100, 100)
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.rect = pygame.Rect(x, y, width, height)

	def draw(self, game_display):
		pygame.draw.rect(game_display, self.color, self.rect)

	
