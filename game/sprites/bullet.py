import pygame


class ShipBullet(pygame.sprite.Sprite):
    def __init__(self ,screen, color, x, y, speed):
        super().__init__()
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(x, y, 5, 10)
        self.speed = speed
        self.screen_width, self.screen_height = self.screen.get_size()

    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()

        pygame.draw.rect(self.screen, self.color ,self.rect)


class AlienBullet(ShipBullet):
    def update(self):
        self.rect.y += self.speed

        if self.rect.top > self.screen_height:
            self.kill()

        pygame.draw.rect(self.screen, self.color ,self.rect)
