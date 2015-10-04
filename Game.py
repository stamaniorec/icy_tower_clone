import pygame
from Camera import Camera
from Player import Player 
from Platform import Platform
from PlatformController import PlatformController

pygame.init()

from Constants import *
from Utils import *
game_display = pygame.display.set_mode(res)
pygame.display.set_caption(GAME_CAPTION)

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

arrow_image = load_image("arrow.png")
selected_option = 0.30

background = load_image('background.jpg')

camera = Camera(player)

game_state = 'Menu'

game_loop = True
clock = pygame.time.Clock()
fps = 60

while game_loop:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				if game_state == 'Playing' or game_state == "Game Over":
					game_state = 'Menu'
			elif game_state == 'Game Over':
				if event.key == pygame.K_SPACE:
					reinit()
					game_state = 'Playing'
			elif game_state == "Menu": #----------------Menu Events-------------
				if event.key == pygame.K_DOWN and selected_option<0.50:
					selected_option+=0.10
				elif event.key == pygame.K_UP and selected_option>0.35:
					selected_option-=0.10
				elif event.key == pygame.K_RETURN:
					if selected_option < 0.35:
						reinit()
						game_state = 'Playing'
					elif selected_option == 0.50:
						game_loop = False

	keys_pressed = pygame.key.get_pressed()
	if keys_pressed[pygame.K_LEFT]:
		player.vel_x = -player.speed
		player.sprite_index_y = 2
	elif keys_pressed[pygame.K_RIGHT]:
		player.vel_x = player.speed
		player.sprite_index_y = 1
	else:
		player.vel_x = 0
		if player.vel_y >= JUMP_VELOCITY/2:
			player.sprite_index_y = 0

	#---------------------------MENU----------------------------
	if game_state == "Menu":
		game_display.blit(background,(0,0))
		game_display.blit(arrow_image, (MENU_START_X + ARROW_HALF_WIDTH, MENU_START_Y + SCREEN_HEIGHT*selected_option - ARROW_HALF_HEIGHT))
		if pygame.font:
			# transparent black rectangle
			s = pygame.Surface((SCREEN_WIDTH/2, round(SCREEN_HEIGHT/1.45)), pygame.SRCALPHA)
			s.fill((0,0,0,128))
			game_display.blit(s, (MENU_START_X, MENU_START_Y))
			# menu title
			message_display(game_display, "Icy Tower(clone)", 0, MENU_START_Y+round(SCREEN_HEIGHT*0.15), 60, white, True)
			# menu items
			message_display(game_display, "Play", 0, MENU_START_Y+round(SCREEN_HEIGHT*0.30), 50, white, True)
			message_display(game_display, "About", 0, MENU_START_Y+round(SCREEN_HEIGHT*0.40), 50, white, True)
			message_display(game_display, "Quit", 0, MENU_START_Y+round(SCREEN_HEIGHT*0.50), 50, white, True)
	
	#-------------------------PLAYING---------------------------
	elif game_state == 'Playing':

		if keys_pressed[pygame.K_SPACE]:
			if player.on_any_platform(platform_controller, floor):
				player.sprite_index_y = 3
				if player.vel_y >= JUMP_VELOCITY/2:
					player.vel_y = -JUMP_VELOCITY

		player.update()
		player.collide_platform(floor)
		platform_controller.collide_set(player)
	
		platform_controller.score = player.score
		camera.update(player.score)
		platform_controller.generate_new_platforms(camera)

		if player.fallen_off_screen(camera):
			game_state = 'Game Over'

			# game_display.fill(black)
			# image = pygame.transform.scale(image, (800,desired_height))
		game_display.blit(background,(0,0))

		floor.draw(game_display, camera)
		platform_controller.draw(game_display, camera)
		player.draw(game_display, camera)
		
		message_display(game_display, str(player.score), 25, 30, 36, white)

	#------------------------GAME OVER--------------------------
	elif game_state == 'Game Over':

		game_display.blit(background,(0,0))
		if pygame.font:
		    message_display(game_display, "GAME OVER", 0, 200, 70, white, True)
		    message_display(game_display, "Score: %d" % player.score, 0, 300, 50, white, True)
		    message_display(game_display, "Press SPACE to play again!", 0, 400, 50, white, True)
		    message_display(game_display, "Press ESC to return to menu!", 0, 500, 40, white, True)


	#-----------------------------------------------------------
	
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()
