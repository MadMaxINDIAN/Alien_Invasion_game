import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien

ai_settings = Settings()


def run_game():
    # Initialise game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")

    # MAKE A SHIP.
    ship = Ship(ai_settings, screen)

    # MAKE A GROUP TO STORE THE BULLETS.
    bullets = Group()
    new_bullets = Group()

    # make a group of aliens
    aliens = Group()

    # create fleet
    gf.create_fleet(ai_settings, screen, aliens)

    # start the main loop for the game.
    while True:
        gf.check_function(ship, ai_settings, screen, new_bullets, bullets)
        ship.update()
        gf.update_bullet(bullets, aliens, ai_settings, screen)
        gf.update_aliens(aliens, ai_settings)
        gf.update_function(ai_settings, screen, ship, bullets, new_bullets, aliens)


run_game()
