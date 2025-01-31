import sys

import pygame

from game import config, groups
from game.main_menu import MainMenu
from game.sprites.alien import AliensGridMaker
from game.sprites.player import Player
from game.ui.button import Button
from game.ui.text import Text

pygame.init()

screen = pygame.display.set_mode(config.window_size)
pygame.display.set_caption("Space Invaders")


clock = pygame.time.Clock()

run = True

background_image = pygame.image.load(config.BACKGROUND)


# ui
game_title = Text(screen, "center", (config.window_center[0], 180), "SPACE INVADERS", 42, config.WHITE, True, "Arial")
play_button = Button(screen, (config.window_center[0], config.window_center[1] - 80), (200, 75), "Play", 36, color=config.BLACK)
quit_button = Button(screen, (config.window_center[0], config.window_center[1] + 10), (200, 75), "Quit", 36, color=config.BLACK)


main_menu = MainMenu(screen, background_image, game_title, play_button, quit_button)


# sprites
player = Player(screen, config.SPACE_SHIP, config.window_center[0] - 30, config.window_size[1] - 45, config.SHIP_SPEED, config.ORANGE, config.BULLET_SPEED)
aliens_grid = AliensGridMaker(screen)
aliens_grid.create(list(config.aliens_imgs.values())[0], config.ALIEN_SPEED)

# TODO: make gameover screen

def game_loop():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(config.BLACK)
        screen.blit(background_image, (0, 0))

        alien_bounds = aliens_grid.get_grid_bounds()
        if alien_bounds is not None:
            left, right = alien_bounds

            if right >= screen.get_width() or left <= 0:
                for alien in groups.aliens:
                    alien.rect.y += 10
                    alien.direction = left <= 0

        lowest_aliens = aliens_grid.get_lowest_active_aliens()
        for alien in lowest_aliens:
            alien_bullet = alien.shoot(screen, "white", config.BULLET_SPEED)
            if alien_bullet:
                groups.alien_bullets.add(alien_bullet)

        groups.aliens.update()

        hits_al = pygame.sprite.groupcollide(groups.ship_bullets, groups.aliens, True, True)
        if hits_al:
            config.explosion.play()
            print("Destroyed")

        hits_pl = pygame.sprite.spritecollide(player, groups.alien_bullets, dokill=True) # type: ignore
        if hits_pl:
            print("Destroyed")
            sys.exit()

        player.update()
        groups.ship_bullets.update()
        groups.alien_bullets.update()


        for bullet in groups.ship_bullets:
            bullet.update()

        pygame.display.flip()

        clock.tick(config.FPS)

def main():
    main_menu.update()
    game_loop()


if __name__ == "__main__":
    main()
