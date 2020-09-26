import pygame
import sys
from bullet import Bullet
from alien import Alien
from pygame.sprite import Sprite


def check_keydown_events(event, ship, ai_settings, screen, new_bullets, bullets):
    """respond to key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet_keydown(ai_settings, bullets, new_bullets, ship, screen)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship, ai_settings, screen, new_bullets, bullets):
    """respond to key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        fire_bullet_keyup(ai_settings, bullets, new_bullets, ship, screen)


def check_function(ship, ai_settings, screen, new_bullets, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, new_bullets, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship, ai_settings, screen, new_bullets, bullets)


def update_function(ai_settings, screen, ship, bullets, new_bullets, aliens):
    """UPDATE IMAGES ON THE SCREEN, AND FLIP THE NEW SCREEN"""
    # REDRAW THE SCREEN DURING EACH PASS THROUGH LOOP
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # ADD ALIEN.
    aliens.draw(screen)

    # ADD NEW BULLETS.
    for new_bullet in new_bullets.sprites():
        bullets.add(new_bullet)
        new_bullets.remove(new_bullet)

    # REDRAW ALL BULETS BEHIND SHIP AND ALIENS.
    for bullet in bullets.sprites():
        bullet.draw_bullets()

    # MAKE THE MOST RECENTLY DRAWN SCREEN VISIBLE
    pygame.display.flip()


def update_bullet(bullets, aliens, ai_settings, screen):
    """update position of bullets."""
    bullets.update()
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        #destroy existing bullets and create new fleet.
        bullets.empty()
        create_fleet(ai_settings, screen, aliens)

    # get rid of bullet which have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


def fire_bullet_keydown(ai_settings, bullets, new_bullets, ship, screen):
    if len(bullets) < ai_settings.bullets_allowed:
        ai_settings.initial_power_of_bullet_keydown = 0
        while ai_settings.initial_power_of_bullet_keydown < ai_settings.final_power_of_bullet_keydown:
            # CREATE A NEW BULLET.
            new_bullet = Bullet(ai_settings, ship, screen)
            new_bullets.add(new_bullet)
            ai_settings.initial_power_of_bullet_keydown += 1


def fire_bullet_keyup(ai_settings, bullets, new_bullets, ship, screen):
    if len(bullets) < ai_settings.bullets_allowed:
        ai_settings.initial_power_of_bullet_keyup = 0
        while ai_settings.initial_power_of_bullet_keyup < ai_settings.final_power_of_bullet_keyup:
            # CREATE A NEW BULLET.
            new_bullet = Bullet(ai_settings, ship, screen)
            new_bullets.add(new_bullet)
            ai_settings.initial_power_of_bullet_keyup += 1


def create_fleet(ai_settings, screen, aliens):
    """create a full fleet of aliens"""
    # create an alien and place it in the row
    # spacing between each alien is equal to one alien
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    # determining how many alien fit in a row
    available_space_x = ai_settings.screen_width - (2 * alien.rect.width)
    number_aliens_x = available_space_x // (2 * alien.rect.width)

    # determinig how many alien fit in a column.
    available_space_y = ai_settings.screen_height - (2 * alien.rect.height)
    number_aliens_y = available_space_y // (2 * alien.rect.height)

    # create the first row.
    number_of_alien = 0
    while number_of_alien < ai_settings.health_of_alien:
        for alien_number_y in range(number_aliens_y - 2):
            for alien_number_x in range(number_aliens_x):
                """create an alien and place it in the row"""
                alien = Alien(ai_settings, screen)
                alien.x = alien_width + 2*alien_width*alien_number_x
                alien.y = alien_height + 2*alien_height*alien_number_y
                alien.rect.x = alien.x
                alien.rect.y = alien.y
                aliens.add(alien)
        number_of_alien += 1


def update_aliens(aliens, ai_settings):
    check_fleet_action(aliens, ai_settings)
    aliens.update()


def check_fleet_direction(aliens, ai_settings):
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_action(aliens, ai_settings):
    """we have to change the direction of the fleet, if one of the alien has touch the edge of the screen"""
    for alien in aliens:
        if alien.check_edges():
            check_fleet_direction(aliens, ai_settings)
