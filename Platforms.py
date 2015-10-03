import pygame
pygame.init()

class Obstacle:
	color = (255, 100, 100)
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.obstacle_rect = pygame.Rect(x, y, width, height)
	def draw(self, gameDisplay):
		pygame.draw.rect(gameDisplay, self.color, self.obstacle_rect)
