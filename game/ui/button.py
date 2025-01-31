from __future__ import annotations

from typing import TypeAlias

import pygame

from game.config import click
from game.groups import buttons
from game.ui.text import Text


class OnClick:
    name = "click"

    def __init__(self, handler):
        self.handler = handler

    def check(self, button_rect: pygame.Rect):
        x, y = pygame.mouse.get_pos()
        inbutton = (
            button_rect.left <= x <= button_rect.right
            and button_rect.top <= y <= button_rect.bottom
        )
        pressed = pygame.mouse.get_pressed()[0]
        if inbutton and pressed:
            click.play()
            return inbutton and pressed

Event: TypeAlias = OnClick

class Button(pygame.sprite.Sprite):
    def __init__(  # noqa: PLR0913
        self,
        screen,
        center_coords: tuple[int, int] | None = None,
        size: tuple[float, float] = (100, 50),
        text="Button",
        font_size=16,
        text_color=(255, 255, 255),
        bold_text=True,
        color=(0, 0, 255),
        border_color=(255, 255, 255),
        border_width=3,
    ):
        super().__init__()

        self.event = None
        self.renderSurface = screen
        self.color = color
        self.borderColor = border_color
        self.borderWidth = border_width

        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()

        if center_coords is None:
            center_coords = screen.get_width() // 2, screen.get_height() // 2
        self.rect.center = center_coords

        self.text = Text(screen, "center", (0, 0), text, font_size, text_color, bold=bold_text)
        self.text.rect.center = self.rect.center

        buttons.add(self)

    def add_event(self, event: Event):
        self.event = event

    def update(self, game_state):
        if self.event and self.event.name == "click" and self.event.check(self.rect):
            self.event.handler(game_state)

        pygame.draw.rect(self.renderSurface, self.borderColor, self.rect)
        pygame.draw.rect(
            self.renderSurface,
            self.color,
            self.rect.inflate(-2 * self.borderWidth, -2 * self.borderWidth),
        )

        self.text.update()
