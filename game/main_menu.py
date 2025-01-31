import sys

import pygame

from game.config import music
from game.groups import buttons, texts
from game.ui.button import OnClick


class MainMenu:
    game_state = {"state": "menu"}

    def __init__(self, screen, background_image, text, *buttons):
        self.screen = screen
        self.background_image = background_image
        self.text = text
        self.buttons = list(buttons)


    def on_play_click(self):
        self.game_state["state"] = "play"

    def on_quit_click(self):
        self.game_state["state"] = "quit"
        sys.exit()

    def update(self):
        self.buttons[0].add_event(OnClick(lambda _: self.on_play_click()))
        self.buttons[1].add_event(OnClick(lambda _: self.on_quit_click()))

        music.play()

        while self.game_state["state"] == "menu":
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background_image, (0, 0))

            buttons.update(self.game_state)
            texts.update()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
