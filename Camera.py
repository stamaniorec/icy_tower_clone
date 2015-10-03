import pygame

from Constants import SCREEN_HEIGHT

class Camera:
	def __init__(self, player):
		self.y = 0
		self.player = player

	def update(self):
		if self.player.y <= SCREEN_HEIGHT / 2:
			self.y = self.player.y - SCREEN_HEIGHT/2
