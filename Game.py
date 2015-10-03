import pygame
from Camera import Camera
from Player import Player 
from Platform import Platform
from PlatformController import PlatformController

pygame.init()

from Constants import *
from Utils import *
game_display = pygame.display.set_mode(res)

black = (0,0,0)
blue = (0,0, 255)
white = (255,255,255)

def reinit():
	global player
	global platform_controller
	global floor
	global camera
	player = Player()
	platform_controller = PlatformController()
	floor = Platform(0, SCREEN_HEIGHT-36, SCREEN_WIDTH, 36)
	camera = Camera(player)

player = Player()
platform_controller = PlatformController()
floor = Platform(0, SCREEN_HEIGHT-36, SCREEN_WIDTH, 36)

background = load_image('background.jpg')

camera = Camera(player)

game_state = 'Playing'

game_loop = True
clock = pygame.time.Clock()
fps = 60

while game_loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_loop = False
		if event.type == pygame.KEYDOWN:
			if game_state == 'Playing':
				if event.key == pygame.K_SPACE and (player.on_any_platform(platform_controller, floor)):
					player.vel_y = -JUMP_VELOCITY
					player.sprite_index_y = 3
				if event.key == pygame.K_ESCAPE:
					game_loop = False
			elif game_state == 'Game Over':
				if event.key == pygame.K_SPACE:
					reinit()
					game_state = 'Playing'

	keys_pressed = pygame.key.get_pressed()
	if(keys_pressed[pygame.K_LEFT]):
		player.vel_x = -player.speed
		player.sprite_index_y = 2
	elif(keys_pressed[pygame.K_RIGHT]):
		player.vel_x = player.speed
		player.sprite_index_y = 1
	else:
		player.vel_x = 0
		player.sprite_index_y = 0

	player.update()
	player.collide_platform(floor)
	platform_controller.collide_set(player)
	
	camera.update()
	platform_controller.generate_new_platforms(camera)

	if player.fallen_off_screen(camera):
		game_state = 'Game Over'

	game_display.fill(black)
	
	if game_state == 'Playing':
		# image = pygame.transform.scale(image, (800,desired_height))
		game_display.blit(background,(0,0))

		floor.draw(game_display, camera)
		platform_controller.draw(game_display, camera)
		player.draw(game_display, camera)
		
		message_display(game_display, str(player.score), 25, 30, 36, white)
	elif game_state == 'Game Over':
		game_display.blit(background,(0,0))
		if pygame.font:
		    message_display(game_display, "GAME OVER", 0, 200, 70, white, True)
		    message_display(game_display, "Score: %d" % player.score, 0, 300, 50, white, True)
		    message_display(game_display, "Press SPACE to play again!", 0, 400, 50, white, True)
	
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()
