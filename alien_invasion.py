import sys 
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class AllienInvasion:
      """class to manage game assets amd behaviour."""

      def __init__(self):
            """Initilize the game, and create game resouses."""
            pygame.init()
            self.settings = Settings()


            #add full screen mode 
            # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            # self.settings.screen_width = self.screen.get_rect().width
            # self.settings.screen_height = self.screen.get_rect().height

            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            pygame.display.set_caption("Allien Invasion")

            self.ship = Ship(self)
            self.bullets = pygame.sprite.Group()
            self.aliens = pygame.sprite.Group() 
            self._create_fleet() 
            #set bg-color
            self.bg_color = (230, 230, 230)


      def _create_fleet(self):
            """create the fleet of aliens."""
            #make an alien
            alien = Alien(self)
            self.aliens.add(alien)
            alien_width = alien.rect.width
            available_space_x = self.settings.screen_width - (2 * alien_width)
            number_aliens_x = available_space_x // (2 * alien_width)


            #create row of aliens
            for alien_number in range (number_aliens_x):
                  alien = Alien(self)
                  alien.x = alien_width + 2 *alien_width * alien_number
                  alien.rect.x = alien.x
                  self.aliens.add(alien)

      def _create_alien(self, alien_number):
            """create alien an placr it in a row"""
            alien = Alien(self)
            alien_width = alien.rect.width
            alien.x = alien_width + 2 *alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)



      


      def  run_game(self):
            """Start the main loop for the game"""
            while True:
                   """Watch keyboard and mouse events"""
                   self._check_events()
                   self.ship.update()
                   self.bullets.update()
                   self._update_screen()


                   #get rid of bullets that have disappeared
                   for bullet in self.bullets.copy():
                         if bullet.rect.bottom <= 0 :
                               self.bullets.remove(bullet)
                  # print(len(self.bullets))
                  

               
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
         elif event.key == pygame.K_SPACE:
                   # Fire the bullets
               self._fire_bullet()

      def _check_keyup_events(self,event):
             """Respond to key release""" 
             if event.key == pygame.K_RIGHT:
                   self.ship.moving_right = False
             elif event.key == pygame.K_LEFT:
                   self.ship.moving_left = False

      def _fire_bullet(self):
            """create new bullet and add it to the bullets group"""
            if len(self.bullets) < self.settings.bullets_allowed:

             new_bullet = Bullet(self)
             self.bullets.add(new_bullet)

      def _update_screen(self):
             """Update images on the screen , and flip to the  ne screen"""
                #redraw the screen during @ pass thru the loop
             self.screen.fill(self.settings.bg_color)
             self.ship.blitme()

             for bullet in self.bullets.sprites():
                   bullet.draw_bullet()

             self.aliens.draw(self.screen)
             


            #Make most recently drawn screen visible.
             pygame.display.flip()
     


if __name__ == '__main__':
      #make a game instance an run the game.
      ai = AllienInvasion()
      ai.run_game()
            
            
           