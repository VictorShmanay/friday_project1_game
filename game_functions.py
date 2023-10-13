import sys
import pygame as pg
from bullet import Bullet


def check_keydown_events(event, settings, screen, ship, bullets):
    """Отслеживает нажатие клавиш"""
    if event.key == pg.K_RIGHT:  # если это кнопка вправо
        ship.moving_right = True  # разрешаем кораблю двигаться вправо
    if event.key == pg.K_LEFT:
        ship.moving_left = True
    if event.key == pg.K_SPACE:  # если нажали на пробел
        fire_bullet(settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pg.K_RIGHT:  # если это кнопка вправо
        ship.moving_right = False  # запрещаем кораблю двигаться вправо
    if event.key == pg.K_LEFT:
        ship.moving_left = False


def check_events(settings, screen, ship, bullets):
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:  # если кто-то нажал на кнопку
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:  # если кнопку отпустили
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, bullets):
    screen.fill(settings.bg_color)  # заливаем экран игры цветом
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    pg.display.flip()  # обновление кадров в игре


def update_bullets(bullets):
    bullets.update()  # применяю метод update ко ВСЕМ ПУЛЯМ В ГРУППЕ
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(settings, screen, ship, bullets):
    """Выпускает пули, пока не достигнуто ограничение по количеству пуль"""
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)  # создать снаряд
        bullets.add(new_bullet)  # добавить его в группу