import pygame

pygame.mixer.init()

# TODO: refactor global pathes to pathlib

# window config
window_size = (1280, 720)
window_center = (window_size[0] // 2, window_size[1] // 2)

# framerate
FPS = 30

# speed
SHIP_SPEED = 13
ALIEN_SPEED = 2
BULLET_SPEED = 7

# damage
BULLET_DAMAGE = 10

# colors
BLACK = 0, 0, 0
ORANGE = 242, 78, 7
WHITE = 255, 255, 255
GRAY = 79, 88, 102

# images
base_route_images = "D:\\Programing\\Python_files\\invaders_space\\Game\\game\\images\\"

BACKGROUND = base_route_images + "background.png"
SPACE_SHIP = base_route_images + "space_ship.png"
EXPLOSION = base_route_images + "explosion.png"

aliens_imgs = {
    "ALIEN1": base_route_images + "alien1.png",
    "ALIEN2": base_route_images + "alien2.png",
    "ALIEN3": base_route_images + "alien3.png",
    "ALIEN4": base_route_images + "alien4.png",
}

# sounds
base_route_sounds = "D:\\Programing\\Python_files\\invaders_space\\Game\\game\\sounds\\"

explosion = pygame.mixer.Sound(base_route_sounds + "explosion.wav")
click = pygame.mixer.Sound(base_route_sounds + "click.wav")
shoot = pygame.mixer.Sound(base_route_sounds + "shoot.wav")
music = pygame.mixer.Sound(base_route_sounds + "game_music.wav")
