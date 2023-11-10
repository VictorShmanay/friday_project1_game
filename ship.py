import pygame as pg
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, settings, screen):
        """Инициализация корабля и установка его в нужную позицию на экране"""
        super().__init__()
        self.ai_settings = settings  # связал класс настроек с классом корабля
        self.screen = screen

        # загрузим картинку корабля
        self.image = pg.image.load('images/ship.png')
        self.rect = self.image.get_rect()  # получаю колижн-модель корабля
        self.screen_rect = self.screen.get_rect()   # получаю границы экрана игры

        # каждый корабль будет появляться посередине экрана внизу
        self.rect.centerx = self.screen_rect.centerx  # центр по горизонтали корабля берется из центра экрана
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False  # по умолчанию он не двигается вправо
        self.moving_left = False  # по умолчанию он не двигается влево

    def update(self):
        """Обновляет позицию корабля"""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # если двигаться вправо можно
            self.rect.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """Рисует корабль на экране игры"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx