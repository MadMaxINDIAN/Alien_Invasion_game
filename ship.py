import pygame


class Ship:

    def __init__(self, ai_settings,  screen):
        """ INITIALISE THE SHIP AND SET ITS STARTING POSITION"""
        self.screen = screen
        self.ai_settings = ai_settings

        # LOAD THE SHIP IMAGE AND HET ITS REACTION.
        self.image = pygame.image.load("images\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # START EACH NEW SHIP AT THE BOTTOM CENTER OF THE SCREEN.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal for the ship;s center.
        self.center = float(self.rect.centerx)

        # MOVEMENT FLAG
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < (self.screen_rect.right - 100):
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.right > 100:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """ DRAW THE SHIP AT ITS CURRENT LOCATION. """
        self.screen.blit(self.image, self.rect)
