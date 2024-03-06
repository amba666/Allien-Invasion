import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """initialize the alien and start its position."""
        super.__init()
        self.screen = ai_game.screen


        #loading the alien image and set its rect attribute.
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()


        #start @ new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        ##store alien's exact horizontal position.
        self.x = float(self.rect.x)