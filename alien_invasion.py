import sys 
import pygame

class AllienInvasion:
      """class ro manage game assets amd behaviour."""

      def __init__(self):
            """Initilize the game, and create game resouses."""
            pygame.init()

            self.screen = pygame.display.set_mode((1200, 800))
            pygame.display.set_caption("Allien Invasion")

      def  run_game(self):
            """Start the main loop for the game"""
            while True:
                   """Watch keyboard and mouse events"""
                   for event in pygame.event.get():
                         if event.type == pygame.QUIT:
                               sys.exit()


                    #Make most recently drawn screen visible.
                   pygame.display.flip()


if __name__ == '__main__':
      #make a game instance an run the game.
      ai = AllienInvasion()
      ai.run_game()
            
            
           