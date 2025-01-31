import pygame

from game.config import shoot
from game.groups import ship_bullets

from .bullet import ShipBullet


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, img, x, y, speed, bullet_color, bullet_speed):  # noqa: PLR0913
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (85, 90))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.bullet_color = bullet_color
        self.bullet_speed = bullet_speed
        self.screen_width, self.screen_height = self.screen.get_size()

        self.last_shot_time = 0
        self.shoot_delay = 1000

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.left < 0:
                self.rect.x = 0

        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.rect.right = min(self.rect.right, self.screen_width)

        elif keys[pygame.K_SPACE]:
            bullet = self.shoot(self.screen, self.bullet_color, self.bullet_speed)
            if bullet:
                shoot.play()
                ship_bullets.add(bullet)

        self.screen.blit(self.image, self.rect)

    def can_shoot(self):
        current_time = pygame.time.get_ticks()
        return current_time - self.last_shot_time >= self.shoot_delay

    def shoot(self, screen, color, bullet_speed):
        if self.can_shoot():
            self.last_shot_time = pygame.time.get_ticks()
            bullet_x = self.rect.centerx-2
            bullet_y = self.rect.top
            return ShipBullet(screen, color, bullet_x, bullet_y, bullet_speed)
        return None
