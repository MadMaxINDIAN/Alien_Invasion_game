import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """create bullet object at the position of the ship"""
    def __init__(self, ai_settings, ship, screen):
        """ create a bullet object at the ship;s current object. """
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.firing = False

        # store bullet's position as a decimal point.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed

    def update(self):
        """MOVE THE BULLET UP THE SCREEN."""
        # UPDATE THE DECIMAL POSITION OF THE BULLET.
        self.y -= self.speed_factor
        # update the rect position.
        self.rect.y = self.y

    def draw_bullets(self):
        """DRAW THE BULLETS TO THE SCREEN."""
        pygame.draw.rect(self.screen, self.color, self.rect)
