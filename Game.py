import pygame
from Player import Player 
from Platform import Platform
from PlatformController import PlatformController

pygame.init()

from Constants import *
game_display = pygame.display.set_mode(res)

black = (0,0,0)
blue = (0, 0, 255)

player = Player()
platform_controller = PlatformController()
floor = Platform(0, SCREEN_HEIGHT-50, SCREEN_WIDTH, 50)

game_loop = True
clock = pygame.time.Clock()
fps = 60

while game_loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and (player.on_platform(platform_controller, floor)):
				player.vel_y = -JUMP_VELOCITY
			if event.key == pygame.K_ESCAPE:
				game_loop = False

	keys_pressed = pygame.key.get_pressed()
	if(keys_pressed[pygame.K_LEFT]):
		player.vel_x = -player.speed
	elif(keys_pressed[pygame.K_RIGHT]):
		player.vel_x = player.speed
	else:
		player.vel_x = 0

	player.update()
	player.collide_platform(floor)	
	platform_controller.collide_set(player)

	game_display.fill(black)
	
	floor.draw(game_display)
	player.draw(game_display)
	platform_controller.draw(game_display)
	
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()
