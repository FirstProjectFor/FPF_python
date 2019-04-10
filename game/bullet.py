import pygame
from pygame.sprite import Sprite

from game.settings import Settings


class Bullet(Sprite):
    """子弹"""

    def __init__(self, setting: Settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(ship.rect.y)

        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

