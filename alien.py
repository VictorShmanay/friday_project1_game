import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца"""
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        # загрузка изображения
        self.image = pg.image.load('images/alien.png').convert_alpha()
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца на экран"""
        self.screen.blit(self.image, self.rect)