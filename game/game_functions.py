import sys
import pygame

from game.settings import Settings


def check_event(ship):
    """检查事件"""
    for event in pygame.event.get():
        check_exit_events(event)
        check_key_down_events(event, ship)
        check_key_up_events(event, ship)


def check_exit_events(event):
    if event.type == pygame.QUIT:
        sys.exit()


def check_key_down_events(event, ship):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ship.moving_left = True


def check_key_up_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False


def update_screen(setting: Settings, screen, ship):
    screen.fill(setting.bg_color)
    ship.blit_me()
    pygame.display.flip()
