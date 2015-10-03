import pygame
from random import randrange
from Platform import Platform
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT, JUMP_VELOCITY
pygame.init()

class PlatformController:
	platform_set = []
	
	def __init__(self):
		for i in range(0, 10):
			self.platform_set.append(self.generate_platform(i))
		self.flags = []
	
	def generate_platform(self, index):
		width = 250
		height = 20
		y = index * 100
		x = randrange(0, SCREEN_WIDTH-width) 
		return Platform(x, y, width, height)

	def draw(self, game_display, camera):
		for p in self.platform_set:
			p.draw(game_display, camera)

	def collide_set(self, player):
		for p in self.platform_set:
			player.collide_platform(p)

	# def generate_new_platforms(self, camera):
	# 	print(self.platform_set[-1].y + camera.y)
	# 	if self.platform_set[-1].y + camera.y < SCREEN_HEIGHT:
	# 		for i in range(0,10):
	# 			self.platform_set.append(self.generate_platform(i))
