import pygame as pg
import game_functions as gf
from settings import Settings
from button import Button
from ship import Ship
from game_stats import GameStats
from pygame.sprite import Group


def run_game():
    ai_settings = Settings()
    stats = GameStats(ai_settings)

    pg.init()  # инициализируем pygame
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # создаем экран игры разрешением 1280х720px
    pg.display.set_caption("Alien Invasion")  # название окна игры

    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)
    aliens = Group()  # создаю список для пришельцев
    bullets = Group()

    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:  # цикл игры
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
            gf.update_aliens(aliens, ai_settings, ship, stats, screen, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button)


run_game()  # вызываем игровую функциювызываем игровую функцию