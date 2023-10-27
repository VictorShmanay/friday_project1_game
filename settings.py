import pygame as pg

class Settings:
    """Класс для настроек игры (всех)"""
    def __init__(self):
        """Инициализация настроек игры"""
        self.screen_width = 1280
        self.screen_height = 800
        self.bg = pg.image.load('images/space.jpg')

        self.ship_speed_factor = 1.5

        # настройки пули
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_speed = 5
        self.bullet_color = (241, 115, 255)
        self.bullets_allowed = 3


        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1