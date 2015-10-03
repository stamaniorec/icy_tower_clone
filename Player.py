import pygame
pygame.init()

from Constants import GRAVITY

class Player:
	x = 30
	y = 10
	width = 30
	height = 30

	vel_x = 5
	vel_y = 0
	max_falling_speed = 20

	color = (255, 0, 0)
	# falling_speed = 10
	# jumping_speed = 0
	speed = 5

	def __init__(self):
		return

	def draw(self, gameDisplay):
		pygame.draw.rect(gameDisplay, self.color, self.get_rect())
	
	def update(self):
		self.x += self.vel_x
		self.y += self.vel_y
		self.vel_y += GRAVITY
		if self.vel_y > self.max_falling_speed:
			self.vel_y = self.max_falling_speed

	def collide_floor(self, floor):
		if self.get_rect().colliderect(floor.rect):
			self.y = floor.rect.top - self.height
	
	def collide_platform(self, platform):
		#if (((self.y + self.height) == range(platform.y, platform.y+platform.height)) and (self.x.range(platform.x, platform.x+platform.width))):
		
		if self.get_rect().colliderect(platform.rect):
			if self.y+self.height >= platform.y:
				self.y = platform.y - self.height

	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)
