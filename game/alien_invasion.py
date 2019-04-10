import pygame
from pygame.sprite import Group

import game.game_functions as gf
from game.settings import Settings
from game.ship import Ship


def run_game():
    """运行游戏"""
    setting = Settings()

    screen = pygame.display.set_mode([setting.screen_width, setting.screen_height])
    ship = Ship(setting, screen)

    bullets = Group()

    # title
    pygame.display.set_caption("Alien Invasion")
    bg_color = (255, 255, 255)

    while True:
        gf.check_event(setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(setting, screen, ship, bullets)


run_game()
