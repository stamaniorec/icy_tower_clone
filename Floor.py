import pygame
pygame.init()
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Floor:
	def __init__(self):
		self.color = (255,255,255)
		self.height = 50
		self.rect = pygame.Rect(0, SCREEN_HEIGHT-self.height, SCREEN_WIDTH, self.height)

	def draw(self, game_display):
		pygame.draw.rect(game_display, self.color, self.rect)
