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

            #add full screen mode 
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

            # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))if self.moving_left and self.rect > 0:
            pygame.display.set_caption("Allien Invasion")

            self.ship = Ship(self)

            #set bg-color
            self.bg_color = (230, 230, 230)


      def  run_game(self):
            """Start the main loop for the game"""
            while True:
                   """Watch keyboard and mouse events"""
                   self._check_events()
                   self.ship.update()
                   self._update_screen()
                  

               
      def _check_events(self):
            """Resposnd to keypresses and mouse events."""
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        sys.exit()

                  elif event.type == pygame.KEYDOWN:
                        self._check_keydown_events(event)

                  elif event.type == pygame.KEYUP:
                      self._check_keyup_events(event)
                               

      def _check_keydown_events(self, event):
             """Respond to the keypresses"""
             if event.key == pygame.K_RIGHT:
                   self.ship.moving_right = True
             elif event.key == pygame.K_LEFT:
                   self.ship.moving_left = True
             elif event.key == pygame.K_q:
                  sys.exit()

      def _check_keyup_events(self,event):
             """Respond to key release""" 
             if event.key == pygame.K_RIGHT:
                   self.ship.moving_right = False
             elif event.key == pygame.K_LEFT:
                   self.ship.moving_left = False

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
            
            
           