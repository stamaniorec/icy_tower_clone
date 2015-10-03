import pygame
from Player import Player 
from Platform import Platform
from Floor import Floor

pygame.init()

from Constants import *
game_display = pygame.display.set_mode(res)

black = (0,0,0)
blue = (0, 0, 255)

player = Player()
platform = Platform(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 80, 10)
floor = Floor()

game_loop = True
clock = pygame.time.Clock()
fps = 60

while game_loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and player.on_floor(floor):
				player.vel_y = -17

	keys_pressed = pygame.key.get_pressed()
	if(keys_pressed[pygame.K_LEFT]):
		player.vel_x = -player.speed
	elif(keys_pressed[pygame.K_RIGHT]):
		player.vel_x = player.speed
	else:
		player.vel_x = 0

	player.update()
	player.collide_floor(floor)
	player.collide_platform(platform)

	if player.collide_platform(platform):
		game_display.fill(blue)
	else:
		game_display.fill(black)

	floor.draw(game_display)
	player.draw(game_display)
	platform.draw(game_display)
	
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()
