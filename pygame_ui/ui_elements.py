# pygame_ui/ui_elements.py

import pygame
from pygame_ui.config import COLORS, FONT_PATH

class Button:
    def __init__(self, text, pos, size=(120, 40), color=COLORS["button"], text_color=COLORS["text"]):
        self.rect = pygame.Rect(pos, size)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(FONT_PATH, 20)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, COLORS["border"], self.rect, 2)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

def show_message(screen, message, pos=(400, 50), color=COLORS["text"], size=28):
    font = pygame.font.Font(FONT_PATH, size)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, text_rect)
