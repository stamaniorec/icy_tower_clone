import pygame
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Text
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(game_display, text, x, y, font_size, color, centered_x=False, centered_y=False):
    font = pygame.font.Font(None,font_size)
    TextSurf, TextRect = text_objects(text, font, color)
    if centered_x and centered_y:
    	TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    elif centered_x:
    	TextRect.center = ((SCREEN_WIDTH/2),y)
    elif centered_y:
    	TextRect.center = (x,(SCREEN_HEIGHT/2))
    else:
    	TextRect.center = (x,y)
    game_display.blit(TextSurf, TextRect)

import os, sys
from pygame.locals import RLEACCEL
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    colorkey = -1
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image