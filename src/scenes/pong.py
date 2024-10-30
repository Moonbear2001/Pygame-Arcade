import pygame
from random import choice

from .scene import Scene


# Paddle settings
PADDLE_SPEED = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_EDGE_OFFSET = 10
LEFT_PADDLE_STARTING_X = PADDLE_EDGE_OFFSET
LEFT_PADDLE_STARTING_Y = 0
RIGHT_PADDLE_STARTING_X = 1280 - PADDLE_EDGE_OFFSET - PADDLE_WIDTH
RIGHT_PADDLE_STARTING_Y = 0

# Ball settings
BALL_SPEED = 10
BALL_SIZE = 20
BALL_STARTING_X = 500
BALL_STARTING_Y = 500


class Pong(Scene):
    """
    An implementation of the classic Pong game.
    """

    name = "pong"

    def __init__(self):
        """
        Initializes a new scene.
        """
        super().__init__()
        self.add_child(
            Paddle(LEFT_PADDLE_STARTING_X, LEFT_PADDLE_STARTING_X, left=True)
        )
        self.add_child(Paddle(RIGHT_PADDLE_STARTING_X, RIGHT_PADDLE_STARTING_X))
        self.add_child(Ball(BALL_STARTING_X, BALL_STARTING_Y))

    def _on_update(self, delta_time):
        pass

    def _on_render(self):
        self.canvas.fill("gray")


class Paddle(Scene):

    custom_watched_events = {pygame.KEYDOWN, pygame.KEYUP}

    def __init__(self, x, y, left=False):
        super().__init__(self.custom_watched_events, x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.left = left
        self.y_vel = 0

    def update(self, delta_time):
        self.rect.move_ip(0, self.y_vel * PADDLE_SPEED)

    def _on_event(self, event):
        if self.left:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.y_vel = -1
                if event.key == pygame.K_s:
                    self.y_vel = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or pygame.K_s:
                    self.y_vel = 0
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.y_vel = -1
                if event.key == pygame.K_UP:
                    self.y_vel = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    self.y_vel = 0

    def _on_render(self):
        pygame.draw.rect(self.canvas, "white", (0, 0, PADDLE_WIDTH, PADDLE_HEIGHT))


class Ball(Scene):

    def __init__(self, x, y):
        super().__init__(left=x, top=y, width=BALL_SIZE, height=BALL_SIZE)
        self.x_vel = self._random_direction()
        self.y_vel = self._random_direction()

    def update(self, delta_time):
        pass

    def _random_direction(self):
        return choice([-1, 1])

    def _on_render(self):
        pygame.draw.ellipse(self.canvas, "white", (0, 0, BALL_SIZE, BALL_SIZE))


# class Paddle(pygame.sprite.Sprite):

#     def __init__(self, width, height, starting_pos):
#         super().__init__()
#         self.rect = pygame.Rect(starting_pos, (width, height))
#         self.image = pygame.Surface((width, height))
#         pygame.draw.rect(self.image, "white", (0, 0, width, height))

#     def update(self, delta_time):
#         pass

# class Ball(pygame.sprite.Sprite):

#     def __init__(self, size, starting_pos):
#         super().__init__()
#         self.rect = pygame.Rect(starting_pos, (size, size))
#         self.image = pygame.Surface((size, size))
#         pygame.draw.ellipse(self.image, "white", (0, 0, size, size))
#         self.x_vel = 1
#         self.y_vel = 1

#     def update(self, delta_time):
#         pass
