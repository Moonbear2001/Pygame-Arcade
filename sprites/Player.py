import pygame


class Player:
    def __init__(self, game, x=0, y=0, width=100, height=100):
        self.game = game
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 10
        self.actions = {"right": False, "left": False, "up": False, "down": False}

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.actions["right"] = True
            if event.key == pygame.K_a:
                self.actions["left"] = True
            if event.key == pygame.K_w:
                self.actions["up"] = True
            if event.key == pygame.K_s:
                self.actions["down"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.actions["right"] = False
            if event.key == pygame.K_a:
                self.actions["left"] = False
            if event.key == pygame.K_w:
                self.actions["up"] = False
            if event.key == pygame.K_s:
                self.actions["down"] = False

    def update(self):
        if self.actions["right"]:
            self.rect.x += self.speed
        if self.actions["left"]:
            self.rect.x -= self.speed
        if self.actions["up"]:
            self.rect.y -= self.speed
        if self.actions["down"]:
            self.rect.y += self.speed 

    def render(self):
        pygame.draw.rect(self.game.canvas, self.game.colors["red"], self.rect)


