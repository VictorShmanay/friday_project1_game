import pygame as pg

class Settings:
    """Класс для настроек игры (всех)"""
    def __init__(self):
        """Инициализация настроек игры"""
        self.screen_width = 1280
        self.screen_height = 800
        self.bg = pg.image.load('images/bg.jpg')

        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # настройки пули
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_speed = 5
        self.bullet_color = (241, 115, 255)
        self.bullets_allowed = 3

        # настройки флота
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1

        self.speedup_scale = 1.1  # увеличение скорости на 10%
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализация настроек, которые меняются в момент игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed = 5
        self.alien_speed_factor = 1

        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает скорость игры"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
