import pygame
from pygame.sprite import Group
from game_stats import GameStats
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")
    stats = GameStats(game_settings, screen)

    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(game_settings, aliens, stats, ship, screen, bullets)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)
run_game()