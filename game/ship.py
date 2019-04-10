import pygame

from game.settings import Settings


class Ship:
    """飞船"""

    def __init__(self, setting: Settings, screen):
        self.setting = setting
        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.setting.ship_speed_factor
        if self.moving_left and (self.rect.left > self.screen_rect.left):
            self.center -= self.setting.ship_speed_factor
        self.rect.centerx = self.center

    def blit_me(self):
        self.screen.blit(self.image, self.rect)
