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
            #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            #self.settings.screen_width = self.screen.get_rect().width
            #self.settings.screen_height = self.screen.get_rect().height

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
            alien_width, alien_height = alien.rect.size
            
            available_space_x = self.settings.screen_width - (2 * alien_width)
            number_aliens_x = available_space_x // (2 * alien_width)


            #determine number of rows  of alien fit on the screen

            ship_height = self.ship.rect.height
            available_space_y = (self.settings.screen_height - (3* alien_height) - ship_height)
            number_rows = available_space_y // (2* alien_height)

            
            #create full fleet of aliens
            for row_number in range(number_rows):
                  for alien_number in range(number_aliens_x):
                        self._create_alien(alien_number, row_number)

            #create row of aliens
            for alien_number in range (number_aliens_x):
                  alien = Alien(self)
                  alien.x = alien_width + 2 *alien_width * alien_number
                  alien.rect.x = alien.x
                  self.aliens.add(alien)

      def _create_alien(self, alien_number, row_number):
            """create alien an placr it in a row"""
            alien = Alien(self)
            alien_width, alien_height= alien.rect.size
            alien.x = alien_width + 2 *alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y  = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)



      


      def  run_game(self):
            """Start the main loop for the game"""
            while True:
                   """Watch keyboard and mouse events"""
                   self._check_events()
                   self.ship.update()
                   self._update_bullets()
                   self._udate_aliens()
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

      def _update_bullets(self):
            """update the position of bullet an get rid of old bullet"""
             #update bullet positions.
            self.bullets.update()

            # get rid if bullet  that have diapera 
            for bullet in self.bullets.copy():
                  if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)


            #check for anybullet that have hit the aliens
            #if so get rid of bullet and alien
            collisions = pygame.sprite.groupcollide(
                  self.bullets, self.aliens, True, True
            )

      def _udate_aliens(self):
            """update the postition of aliens in the fleet"""
            self._check_fleet_edges()
            self.aliens.update()


      def _check_fleet_edges(self):
            """respond appropriately if any aliens have reaced an edge"""
            for alien in self.aliens.sprites():
                  if alien.check_edges():
                        self._change_fleet_direction()
                        break
      
      def _change_fleet_direction(self):
            """drop entire fleet and change the fleet direction"""
            for alien in self.aliens.sprites():
                  alien.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1

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
            
            
           