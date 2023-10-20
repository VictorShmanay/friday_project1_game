import sys
import pygame as pg
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, settings, screen, ship, bullets):
    """Отслеживает нажатие клавиш"""
    if event.key == pg.K_RIGHT:  # если это кнопка вправо
        ship.moving_right = True  # разрешаем кораблю двигаться вправо
    if event.key == pg.K_LEFT:
        ship.moving_left = True
    if event.key == pg.K_SPACE:  # если нажали на пробел
        fire_bullet(settings, screen, ship, bullets)
    if event.key == pg.K_q:  # быстрый выход из игры
        sys.exit()


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


def update_screen(settings, screen, ship, bullets, aliens):
    #screen.fill(settings.bg_color)  # заливаем экран игры цветом
    screen.blit(settings.bg, (0, 0))
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
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


def get_number_aliens(settings, alien_width):
    available_space = settings.screen_width - 2 * alien_width
    number_aliens = int(available_space / (2 * alien_width))
    return number_aliens


def get_number_rows(settings, ship_height, alien_height):
    available_space_y = settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + (2 * alien_width) * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)


def create_fleet(settings, screen, aliens, ship):
    """Создает флот пришельцев"""
    alien = Alien(settings, screen)
    number_aliens = get_number_aliens(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens):
            create_alien(settings, screen, aliens, alien_number, row_number)