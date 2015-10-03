import pygame
from Player import Player 
from Obstacle import Obstacle
from Floor import Floor

pygame.init()

from Constants import *
game_display = pygame.display.set_mode(res)

black = (0,0,0)
blue = (0, 0, 255)

player = Player()
obstacle = Obstacle(SCREEN_WIDTH/2, SCREEN_HEIGHT-100, 10, 80)
floor = Floor()

game_loop = True
clock = pygame.time.Clock()
fps = 60

while game_loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and player.onfloor():
				player.jump()

	player.update()
	player.collide_floor(floor)
	# if(player.y<SCREEN_HEIGHT-(floor.rect.height + player.height)):
	# 	player.fall()
	player.y -= player.jumping_speed
	if(player.jumping_speed>0):
		player.jumping_speed-=1
	if player.get_rect().colliderect(obstacle.obstacle_rect):
		game_display.fill(blue)
	else:
		game_display.fill(black)
	player.draw(game_display)
	obstacle.draw(game_display)
	
	keys_pressed = pygame.key.get_pressed()
	if(keys_pressed[pygame.K_LEFT]):
		player.x-=player.speed
	elif(keys_pressed[pygame.K_RIGHT]):
		player.x+=player.speed

	floor.draw(game_display)
	
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()
