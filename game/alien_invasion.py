import pygame
from pygame.sprite import Group

import game.game_functions as gf
from game.settings import Settings
from game.ship import Ship


def run_game():
    """运行游戏"""
    setting = Settings()

    screen = pygame.display.set_mode([setting.screen_width, setting.screen_height])
    # 飞船
    ship = Ship(setting, screen)
    # 子弹
    bullets = Group()
    # 外星人
    aliens = Group()
    gf.create_fleet(setting, screen, ship, aliens)

    # title
    pygame.display.set_caption("Alien Invasion")
    bg_color = (255, 255, 255)

    while True:
        gf.check_event(setting, screen, ship, bullets)
        ship.update()
        gf.update_aliens(setting, aliens)
        gf.update_bullets(bullets)
        gf.update_screen(setting, screen, ship, bullets, aliens)


run_game()
