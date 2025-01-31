import pygame

from game.groups import texts


class Text(pygame.sprite.Sprite):
    def __init__(  # noqa: PLR0913
        self,
        screen,
        alignment="center",
        coords: tuple[int, int] = (0, 0),
        text="",
        font_size=16,
        color=(0, 0, 0),
        bold=False,
        font="Arial",
    ) -> None:
        super().__init__()

        self.surface = screen
        self.color = color
        self.font = pygame.font.SysFont(font, font_size, bold)
        self.value = text

        self.rect = pygame.Rect((0, 0), (0, 0))
        self.alignment = alignment
        self.text = text

        if alignment == "center":
            self.rect = self.image.get_rect(center=coords)

        texts.add(self)

    @property
    def text(self):
        return self.value

    @text.setter
    def text(self, new_text) -> None:
        self.image = self.font.render(str(new_text), 1, self.color)
        if self.rect is not None:
            if self.alignment == "center":
                self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.rect = self.image.get_rect()

        self.value = new_text

    def update(self):
        self.surface.blit(self.image, self.rect)
