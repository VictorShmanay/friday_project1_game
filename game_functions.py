import sys
import pygame as pg

def check_keydown_events(event, ship):
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    if event.key == pg.K_RIGHT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    if event.key == pg.K_RIGHT:
        ship.moving_left = False

def check_events(ship):
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                ship.moving_right = True
            elif event.key == pg.K_UP:
                check_keydown_events(event, ship)
        elif event.type == pg.KEYUP:
                check_keyup_events(event, ship)


def update_screen(settings, screen, ship):
    screen.fill(settings.bg_color)  # заливаем экран игры цветом
    ship.blitme()
    pg.display.flip()