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

            
            
           