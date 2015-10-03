import pygame
from IceSprite import IceSprite
pygame.init()

from copy import deepcopy

class Platform:
	color = (255, 100, 100)
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.rect = pygame.Rect(x, y, width, height)
		self.collected_score = False

	def draw(self, game_display, camera):
		rect = deepcopy(self.rect)
		rect.top -= camera.y
		pygame.draw.rect(game_display, self.color, rect)
		for i in range(self.x, self.x+self.width, 10):
			sprite = IceSprite([i, self.y - camera.y])
			game_display.blit(sprite.image, sprite.rect)	
