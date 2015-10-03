import pygame
from random import randrange
from Platform import Platform
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT, JUMP_VELOCITY, MAX_JUMP
pygame.init()

class PlatformController:
	def __init__(self):
		self.platform_set = []
		self.index = 10
		self.last_x = MAX_JUMP
		for i in range(0, self.index):
			self.platform_set.append(self.generate_platform(i))
		for p in self.platform_set:
			print(p.x)
	
	def generate_platform(self, index):
		width = 200
		height = 20
		y = 600 - index * 100
		while True:
			x = randrange(self.last_x-MAX_JUMP , self.last_x+MAX_JUMP+width)
			if x >= 0 and x <= SCREEN_WIDTH - width:
				break
		self.last_x = x
		return Platform(x, y, width, height)

	def draw(self, game_display, camera):
		for p in self.platform_set:
			p.draw(game_display, camera)

	def collide_set(self, player):
		for p in self.platform_set:
			player.collide_platform(p)

	def generate_new_platforms(self, camera):
		if self.platform_set[-1].y - camera.y > -50:
			for i in range(self.index,self.index+10):
				self.platform_set.append(self.generate_platform(i))
			self.index += 10
