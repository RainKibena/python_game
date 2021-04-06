import sys
import pygame
def check_events():
    """Check keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(game_settings, screen, ship):
    """Update image on screen and draw new screen"""
    screen.fill(game_settings.bg_color)
    ship.blitme()
    pygame.display.flip()