import sys
import pygame as pg
from bullet import Bullet
from alien import Alien
from time import sleep


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


def check_events(settings, screen, ship, bullets, stats, btn, aliens, sb):
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:  # если кто-то нажал на кнопку
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:  # если кнопку отпустили
            check_keyup_events(event, ship)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            check_play_button(stats, btn, mouse_x, mouse_y, settings, screen, ship, bullets, aliens, sb)


def check_play_button(stats, btn, mouse_x, mouse_y, settings, screen, ship, bullets, aliens, sb):
    """Запускает новую игру при нажатии на кнопку"""
    button_clicked = btn.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()
        pg.mouse.set_visible(False)  # скрыть курсор после нажатия на кнопку
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, aliens, ship)
        ship.center_ship()

        sb.prep_level()
        sb.prep_score()
        sb.prep_ships()



def update_screen(settings, screen, ship, bullets, aliens, stats, btn, sb):
    #screen.fill(settings.bg_color)  # заливаем экран игры цветом
    screen.blit(settings.bg, (0, 0))
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # вывод очков
    sb.show_score()

    if not stats.game_active:
        btn.draw_button()
    pg.display.flip()  # обновление кадров в игре


def update_bullets(bullets, aliens, settings, screen, ship, sb, stats):
    bullets.update()  # применяю метод update ко ВСЕМ ПУЛЯМ В ГРУППЕ
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(bullets, aliens, settings, screen, ship, sb, stats)


def check_bullet_alien_collision(bullets, aliens, settings, screen, ship, sb, stats):
    """Обработка коллизий пуль с пришельцами"""
    collisions = pg.sprite.groupcollide(bullets, aliens, True, True)
    # groupcollide - определяет столкновение экземпляров двух групп, параметры True отвечают за то, чтобы убрать группы а и б
    for aliens in collisions.values():
        stats.score += settings.alien_points * len(aliens)
    sb.prep_score()
    if len(aliens) == 0:
        # уничтожаем существующие пули и обновляем флот
        stats.level += 1
        sb.prep_level()
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings, screen, aliens, ship)


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


def check_fleet_edges(settings, aliens):
    """Реагирует на достижение одним из пришельцев из флота края экрана"""
    for alien in aliens.sprites():  # перебираю флот пришельцев
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break  # выход из цикла нужен, чтобы пришельцы не перелетали друг через друга


def change_fleet_direction(settings, aliens):
    """Спускает флот и меняет направление движения"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def update_aliens(aliens, settings, ship, stats, screen, bullets, sb):
    """Обновляет позиции всех пришельцев во флоте"""
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pg.sprite.spritecollideany(ship, aliens):  # если столкнулись с кораблем
        ship_hit(settings, stats, screen, ship, aliens, bullets, sb)

    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb)


def ship_hit(settings, stats, screen, ship, aliens, bullets, sb):
    """Обрабатывает столкновения пришельцев и корабля"""
    if stats.ships_left > 1:
        stats.ships_left -= 1
        sb.prep_ships()

        aliens.empty()  # очищаем группу пришельцев
        bullets.empty()  # очищаем группу пуль

        create_fleet(settings, screen, aliens, ship)  # создаем новый флот
        ship.center_ship()  # устанавливаем корабль посередине

        sleep(1)  # замораживаем игру на 1 секунду
    else:
        stats.game_active = False
        pg.mouse.set_visible(True)  # показать курсор после проигрыша


def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb):
    """Проверка столкновения пришельцев с нижним краем экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets, sb)
            break