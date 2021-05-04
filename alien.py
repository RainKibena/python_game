import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for alien description"""
    def __init__(self, game_settings, screen):
        """Create alien object and define its start position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        # load alien image and set rect atribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # set alien position
        self.x = float(self.rect.x)
    def blitme(self):
        """Draw alien at his position"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """Update alien position to right or left"""
        self.x += self.game_settings.alien_speed_factor * self.game_settings.fleet_direction
        self.rect.x = self.x
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True