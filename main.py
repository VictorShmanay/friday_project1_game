
import pygame as pg
import game_functions as gf
from settings import Settings
from ship import Ship
def run_game():
    ai_settings = Settings()

    pg.init()  # инициализируем pygame
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # создаем экран игры разрешением 1280х720px
    pg.display.set_caption("Alian Invasion")
    ship = Ship(screen)

    
    while True:  # цикл игры
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)




run_game()