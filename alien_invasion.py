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
                   self._check_events()
                   self._update_screen()
                  

               
      def _check_events(self):
            """Resposnd to keypresses and mouse events."""
            for event in pygame.event.get():
                         if event.type == pygame.QUIT:
                               sys.exit()

                         elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                       #move the ship tothe right
                                       self.ship.rect.x += 1

      def _update_screen(self):
             """Update images on the screen , and flip to the  ne screen"""
                #redraw the screen during @ pass thru the loop
             self.screen.fill(self.settings.bg_color)
             self.ship.blitme()


                    #Make most recently drawn screen visible.
             pygame.display.flip()
     


if __name__ == '__main__':
      #make a game instance an run the game.
      ai = AllienInvasion()
      ai.run_game()
            
            
           