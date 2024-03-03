import sys 
import pygame

from settings import Settings
from ship import Ship
class AllienInvasion:
      """class ro manage game assets amd behaviour."""

      def __init__(self):
            """Initilize the game, and create game resouses."""
            pygame.init()
            self.settings = Settings()

            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            pygame.display.set_caption("Allien Invasion")

            self.ship = Ship(self)

            #set bg-color
            self.bg_color = (230, 230, 230)


      def  run_game(self):
            """Start the main loop for the game"""
            while True:
                   """Watch keyboard and mouse events"""
                   for event in pygame.event.get():
                         if event.type == pygame.QUIT:
                               sys.exit()

                  #redraw the screen during @ pass thru the loop
                   self.screen.fill(self.settings.bg_color)
                   self.ship.blitme()


                    #Make most recently drawn screen visible.
                   pygame.display.flip()


if __name__ == '__main__':
      #make a game instance an run the game.
      ai = AllienInvasion()
      ai.run_game()
            
            
           