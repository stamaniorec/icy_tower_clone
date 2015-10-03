import pygame
from Camera import Camera
from Player import Player 
from Platform import Platform
from PlatformController import PlatformController

pygame.init()

from Constants import *
game_display = pygame.display.set_mode(res)

black = (0,0,0)
blue = (0, 0, 255)

def reinit():
	global player
	global platform_controller
	global floor
	global camera
	player = Player()
	platform_controller = PlatformController()
	floor = Platform(0, SCREEN_HEIGHT-50, SCREEN_WIDTH, 50)
	camera = Camera(player)

player = Player()
platform_controller = PlatformController()
floor = Platform(0, SCREEN_HEIGHT-50, SCREEN_WIDTH, 50)

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
				if event.key == pygame.K_ESCAPE:
					game_loop = False
			elif game_state == 'Game Over':
				if event.key == pygame.K_SPACE:
					reinit()
					game_state = 'Playing'

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
	
	camera.update()
	platform_controller.generate_new_platforms(camera)

	if player.fallen_off_screen(camera):
		game_state = 'Game Over'

	game_display.fill(black)
	
	if game_state == 'Playing':
		floor.draw(game_display, camera)
		platform_controller.draw(game_display, camera)
		player.draw(game_display, camera)
	elif game_state == 'Game Over':
		font_size = 36
		text_color = (255,255,255)
		background_text_color = (0,0,0)
		background = pygame.Surface(game_display.get_size())
		if pygame.font:
		    font = pygame.font.Font(None, font_size)
		    text = font.render("Press SPACE to play again", 1, text_color, background_text_color) # color and background
		    textpos = text.get_rect(centerx=background.get_width()/2, centery=background.get_height()/2)
		    background.blit(text, textpos)
		    game_display.blit(background, (0,0))
	
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()
