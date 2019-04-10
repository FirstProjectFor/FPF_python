import sys
import pygame
from pygame.sprite import Group

from game.ship import Ship
from game.settings import Settings
from game.bullet import Bullet


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


def update_screen(setting: Settings, screen, ship, bullets):
    screen.fill(setting.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blit_me()

    pygame.display.flip()
