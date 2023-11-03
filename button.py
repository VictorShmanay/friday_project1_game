import pygame as pg


class Button:
    def __init__(self, settings, screen, msg):
        """Инициализация кнопки"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # размеры и свойства кнопки
        self.width, self.height = 200, 50
        self.color = (233, 255, 89)
        self.text_color = (0, 0, 0)
        self.font = pg.font.SysFont(None, 48)

        # создаем объект прямоугольник для кнопки
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # сообщение кнопки создаем один раз
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает по центру кнопки"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)