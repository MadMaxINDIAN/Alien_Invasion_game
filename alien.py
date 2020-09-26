import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """a class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """ initialise the alien and set its starting position """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """load an alien;s image and load its rect attribute"""
        self.image = pygame.image.load("images\ship_alien.bmp")
        self.rect = self.image.get_rect()

        #
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.right
        self.rect.y = self.screen_rect.top

        # start each new alien from top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien;s exact position
        self.x = float(self.rect.x)

        # moving right
        self.moving_right = True
        self.moving_left = False

    def blitme(self):
        """DRAW THE ALIEN AT THE CUREENT POSITION"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move the alien right or left"""
        self.x += self.ai_settings.alien_speed*self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """return true if alien is on the edge of the screen"""
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
