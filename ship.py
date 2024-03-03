import pygame

class Ship:
    """manage the ship."""
    def __init__(self,ai_game):
        """Initialize the postition of the ship  and set its tsrt position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.mbp')
        self.rect = self.image.get_rect()

        #start @ new ship[ a the btn center of the screen.

        self.rect.midbottom = self.image.get_rect()

    def blitme(self):
        """Draw a ship at tis current location."""
        self.screen.blit(self.image, self.rect)


