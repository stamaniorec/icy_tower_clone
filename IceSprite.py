import pygame 

class IceSprite(pygame.sprite.Sprite):
	image = None

	def __init__(self, location):
		pygame.sprite.Sprite.__init__(self)

		if IceSprite.image is None:
			IceSprite.image = pygame.image.load("pics/ice.png")
		
		self.image = IceSprite.image

		self.rect = self.image.get_rect()
		self.rect.topleft = location
