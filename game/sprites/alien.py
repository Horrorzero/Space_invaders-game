import random

import pygame

from game.config import EXPLOSION
from game.groups import aliens
from game.sprites.bullet import AlienBullet


class Alien(pygame.sprite.Sprite):
    def __init__(self, screen, img, x, y, speed):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (69, 55))
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = speed
        self.screen_width, self.screen_height = self.screen.get_size()
        self.direction = True
        self.last_shot_time = 0
        self.shoot_delay = random.randint(1000, 3000)  # noqa: S311
        self.explosion_image = pygame.image.load(EXPLOSION)
        self.exploding = False
        self.explosion_time = 0

    def update(self):
        if self.exploding and pygame.time.get_ticks() > self.explosion_time:
            self.kill()

        if self.direction:
            self.rect.x += self.speed
            if self.rect.right >= self.screen_width:
                self.direction = False
        else:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.direction = True

        self.screen.blit(self.image, self.rect)


    def explode(self):
        if not self.exploding:
            self.image = self.explosion_image
            self.exploding = True
            self.explosion_time = pygame.time.get_ticks() + 500


    def can_shoot(self):
        current_time = pygame.time.get_ticks()
        return current_time - self.last_shot_time >= self.shoot_delay

    def shoot(self, screen, color, bullet_speed):
        if self.can_shoot():
            self.last_shot_time = pygame.time.get_ticks()
            bullet_x = self.rect.centerx-2
            bullet_y = self.rect.bottom
            return AlienBullet(screen, color, bullet_x, bullet_y, bullet_speed)
        return None


class AliensGridMaker:
    def __init__(  # noqa: PLR0913
        self,
        screen,
        start_x = 75,
        start_y = 80,
        gap_x = 80,
        gap_y = 70,
        rows = 2,
        columns = 15,
    ):
        self.screen = screen
        self.start_x = start_x
        self.start_y = start_y
        self.gap_x = gap_x
        self.gap_y = gap_y
        self.rows = rows
        self.columns = columns

    def create(self, img, speed):
        for row in range(self.rows):
            for col in range(self.columns):
                alien_x = self.start_x + col * self.gap_x
                alien_y = self.start_y + row * self.gap_y
                alien = Alien(self.screen, img, alien_x, alien_y, speed)
                aliens.add(alien)
    # TODO: to move logic from the main into the class
    def update(self):
        pass

    @staticmethod
    def get_grid_bounds():
        if not aliens:
            return None

        rects = [sprite.rect for sprite in aliens]

        left = min(rect.left for rect in rects)
        right = max(rect.right for rect in rects)

        return left, right

    @staticmethod
    def get_lowest_active_aliens():
        columns = {}
        for alien in aliens:
            col_x = alien.rect.centerx  # Ідентифікація колони за X-координатою
            if col_x not in columns:
                columns[col_x] = []
            columns[col_x].append(alien)

        # Сортувати по вертикалі (Y-координата)
        for col in columns.values():
            col.sort(key=lambda alien: alien.rect.y, reverse=True)  # Від низу до верху

        lowest_aliens = []

        for col in columns.values():
            if col:  # Якщо є прибульці у колоні
                lowest_aliens.append(col[0])  # Взяти найнижчого

        return lowest_aliens
