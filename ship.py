import pygame

class Ship:
    """Manage the ship."""
    def __init__(self, ai_game):
        """Initialize the position of the ship and set its start position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        # Start the new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ships's horizontal position.
        self.x = float(self.rect.x)

        #moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship position based on the flag"""
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.x +=  self.settings.ship_speed
        if self.moving_left and self.rect > 0:
            self.x -=  self.settings.ship_speed
        #update rect obj from self.x.
        self.rect.x = self.x
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)