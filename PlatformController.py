import pygame
from random import randrange
from Platform import Platform
from Constants import SCREEN_WIDTH, JUMP_VELOCITY, MAX_JUMP
pygame.init()

class PlatformController:
	platform_set = []	

	def __init__(self):
		self.last_x = MAX_JUMP
		for i in range(0, 10):
			self.platform_set.append(self.generate_platform(i))
		self.flags = []
	
	def generate_platform(self, index):
		width=70
		height=20
		y = index * 100
		x = randrange(self.last_x-MAX_JUMP , self.last_x+MAX_JUMP+width) #SCREEN_WIDTH-width)
		self.last_x = x
		return Platform(x, y, width, height)

	def draw(self, game_display):
		for p in self.platform_set:
			p.draw(game_display)

	def collide_set(self, player):
		for p in self.platform_set:
			player.collide_platform(p)
