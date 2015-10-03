import pygame
pygame.init()

from Constants import gravity

class Player:
	x = 30
	y = 10
	width = 30
	height = 30
	color = (255, 0, 0)
	falling_speed = 10
	jumping_speed = 0
	speed = 5

	def __init__(self):
		return
	def draw(self, gameDisplay):
		pygame.draw.rect(gameDisplay, self.color, self.get_rect())
	
	def jump(self):
		self.jumping_speed = 3*self.falling_speed
	
	def update(self):
		self.y += gravity

	def collide_floor(self, floor):
		if self.get_rect().colliderect(floor.rect):
			self.y = floor.rect.top - self.height

	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)

