import pygame as pg
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """Класс для вывода игровой информации"""
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)
        self.prep_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразует текущий счет в игре в картинку"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.text_color,
                                          self.settings.bg_color)
        # выводим счет в верхнем углу
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """Преобразует текущий уровень в игре в картинку"""
        self.level_img = self.font.render('lvl: ' + str(self.stats.level), True, self.text_color,
                                          self.settings.bg_color)
        # выводим счет в верхнем углу
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Сообщает количество оставшихся кораблей"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Вывод очков на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)