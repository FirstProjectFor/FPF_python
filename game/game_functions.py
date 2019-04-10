import sys

import pygame
from pygame.sprite import Group

from game.alien import Alien
from game.bullet import Bullet
from game.settings import Settings
from game.ship import Ship


def check_event(setting: Settings, screen, ship: Ship, bullets: Group):
    """检查事件"""
    for event in pygame.event.get():
        check_exit_events(event)
        check_key_down_events(event, setting, screen, ship, bullets)
        check_key_up_events(event, ship, bullets)


def check_exit_events(event):
    if event.type == pygame.QUIT:
        sys.exit()


def check_key_down_events(event, setting, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(setting, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()


def fire_bullet(setting, screen, ship, bullets):
    if len(bullets) < setting.bullet_count:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)


def check_key_up_events(event, ship, bullets):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            pass


def update_bullets(bullets: Group):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.top <= 0:
            bullets.remove(bullet)


def create_fleet(setting: Settings, screen, ship, alias):
    alien = Alien(setting, screen)
    number_aliens_x = get_numbers_alien_x(setting, alien.rect.width)
    number_row = get_number_rows(setting, ship.rect.height, alien.rect.height)

    for row_number in range(0, number_row):
        for alien_number in range(0, number_aliens_x):
            create_alien(setting, screen, alias, row_number, alien_number)


def get_numbers_alien_x(setting, alien_width):
    """获取每行创建的外星人数量"""
    available_width_x = setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_width_x / (alien_width * 2))
    return number_aliens_x


def create_alien(setting, screen, aliens, row_number, alien_number):
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def get_number_rows(setting: Settings, ship_height, alien_height):
    available_space_y = setting.screen_height - (5 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(setting: Settings, aliens: Group):
    check_fleet_edges(setting, aliens)
    aliens.update()


def check_fleet_edges(setting, aliens: Group):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(setting, aliens)
            break


def change_fleet_direction(setting: Settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += setting.fleet_drop_factor

    setting.fleet_direction *= -1


def update_screen(setting: Settings, screen, ship, bullets, aliens):
    screen.fill(setting.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)

    ship.blit_me()

    pygame.display.flip()
