import pygame as pg


class Ship:
    def __unit__(self, screen):

        self.screen = screen



        self.image = pg.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.botom = self.screen_rect.bottom

    def blitme(selfself):
        self.screen.blit(self.image, self.rect)


