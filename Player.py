import pygame
pygame.init()

from Constants import GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT

from copy import deepcopy

class Player:
	width = 30
	height = 50

	vel_x = 5
	vel_y = 0
	max_falling_speed = 20

	color = (255, 0, 0)
	speed = 5

	def __init__(self):
		self.x = 30
		self.y = 300
		self.score = -10 # negate floor platform

	def draw(self, game_display, camera):
		rect = deepcopy(self.get_rect())
		rect.top -= camera.y
		pygame.draw.rect(game_display, self.color, rect)
	
	def update(self):
		self.x += self.vel_x
		self.y += self.vel_y
		self.vel_y += GRAVITY
		if self.vel_y > self.max_falling_speed:
			self.vel_y = self.max_falling_speed
		if self.x <= 0:
			self.x = 0
		if self.x + self.width >= SCREEN_WIDTH:
			self.x = SCREEN_WIDTH - self.width

	def on_platform(self, platform):
		# return platform.rect.top <= self.y + self.height
		return platform.rect.collidepoint((self.x, self.y + self.height)) or \
			platform.rect.collidepoint((self.x+self.width, self.y + self.height))

	def on_any_platform(self, platform_controller, floor):
		for p in platform_controller.platform_set:
			if self.on_platform(p):
				return True
		if self.on_platform(floor):
			return True
		return False
	
	def collide_platform(self, platform):
		for i in range(0,self.vel_y):
			if pygame.Rect(self.x, self.y-i, self.width, self.height).colliderect(platform.rect):
				if platform.rect.collidepoint((self.x, self.y + self.height-i)) or \
		 	platform.rect.collidepoint((self.x+self.width, self.y + self.height-i)): #do not change! no on_platform here
					self.y = platform.y - self.height
					if not platform.collected_score:
						self.score += 10
						platform.collected_score = True
					# break

	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)

	def fallen_off_screen(self, camera):
		if self.y - camera.y + self.height >= SCREEN_HEIGHT:
			return True
		return False
