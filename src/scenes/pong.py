import pygame
from random import choice

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from .scene import Scene
from utilities import render_text


# Paddle settings
PADDLE_SPEED = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_EDGE_OFFSET = 10
LEFT_PADDLE_STARTING_X = PADDLE_EDGE_OFFSET
LEFT_PADDLE_STARTING_Y = 0
RIGHT_PADDLE_STARTING_X = CANVAS_WIDTH - PADDLE_EDGE_OFFSET - PADDLE_WIDTH
RIGHT_PADDLE_STARTING_Y = 0

# Ball settings
BALL_START_SPEED = 10
BALL_SIZE = 20
BALL_STARTING_X = 500
BALL_STARTING_Y = 500

# Score text
SCORE_EDGE_OFFSET = 50
LEFT_SCORE_POS = (SCORE_EDGE_OFFSET, SCORE_EDGE_OFFSET)
RIGHT_SCORE_POS = (CANVAS_WIDTH - SCORE_EDGE_OFFSET, SCORE_EDGE_OFFSET)

# Game settings
END_SCORE = 10


class Pong(Scene):
    """
    An implementation of the classic Pong game.
    """

    name = "pong"

    def __init__(self, single_player=True, difficulty=4):
        """
        Difficulty can be 1-n, describes how much faster the computer paddle is than the
        player paddle.
        """
        super().__init__()
        self.single_player = single_player

        self.left_score = 0
        self.right_score = 0

        # Setup left paddle and ball
        self.left_paddle = PlayerPaddle(LEFT_PADDLE_STARTING_X, LEFT_PADDLE_STARTING_Y)
        self.ball = Ball(BALL_STARTING_X, BALL_STARTING_Y)
        self.add_child(self.left_paddle)
        self.add_child(self.ball)

        # Should the right paddle be computer controlled?
        if single_player:
            self.right_paddle = ComputerPaddle(
                RIGHT_PADDLE_STARTING_X, RIGHT_PADDLE_STARTING_Y, difficulty
            )
        else:
            self.right_paddle = PlayerPaddle(
                RIGHT_PADDLE_STARTING_X, RIGHT_PADDLE_STARTING_Y, left=False
            )
        self.add_child(self.right_paddle)

    def _on_update(self, delta_time):

        # Ball collision with edge
        if self.ball.rect.left <= 0:
            self._reset_game()
            self.right_score += 1
        elif self.ball.rect.right >= CANVAS_WIDTH:
            self._reset_game()
            self.left_score += 1

        # Ball collision with paddle
        if self.left_paddle.rect.colliderect(
            self.ball
        ) or self.right_paddle.rect.colliderect(self.ball):
            self.ball.x_vel *= -1
            self.ball.speed += 1

        # If playing in single player let the computer move
        if self.single_player:
            self.right_paddle.update_ai(self.ball)

    def _on_render(self):
        self.canvas.fill("black")
        render_text(
            self.canvas, str(self.left_score), "roboto", "white", LEFT_SCORE_POS, 40
        )
        render_text(
            self.canvas, str(self.right_score), "roboto", "white", RIGHT_SCORE_POS, 40
        )

    def _reset_game(self):
        self.ball.reset()


class Paddle(Scene):
    """
    Functionality of a paddle independent of movement control.
    """

    def __init__(self, x, y):
        super().__init__(left=x, top=y, width=PADDLE_WIDTH, height=PADDLE_HEIGHT)
        self.y_vel = 0

    def _on_render(self):
        pygame.draw.rect(self.canvas, "white", (0, 0, PADDLE_WIDTH, PADDLE_HEIGHT))


class PlayerPaddle(Paddle):
    """
    Paddle controlled by the player.
    """

    def __init__(self, x, y, left_side=True):
        super().__init__(x, y)
        self.left_side = left_side

    def _on_update(self, delta_time):
        keys = pygame.key.get_pressed()
        if self.left_side:
            if keys[pygame.K_w] and self.rect.top - PADDLE_SPEED >= 0:
                self.rect.y -= PADDLE_SPEED
            if keys[pygame.K_s] and self.rect.bottom + PADDLE_SPEED <= CANVAS_HEIGHT:
                self.rect.y += PADDLE_SPEED
        else:
            if keys[pygame.K_UP] and self.rect.top - PADDLE_SPEED >= 0:
                self.rect.y -= PADDLE_SPEED
            if keys[pygame.K_DOWN] and self.rect.bottom + PADDLE_SPEED <= CANVAS_HEIGHT:
                self.rect.y += PADDLE_SPEED
        self.rect.move_ip(0, self.y_vel * PADDLE_SPEED)


class ComputerPaddle(Paddle):
    """
    Paddle controlled by the computer.
    """

    def __init__(self, x, y, difficulty):
        super().__init__(x, y)
        self.difficulty = difficulty

    def update_ai(self, ball):
        """
        Move the paddle to track the ball.
        """
        if ball.rect.centery > self.rect.centery and self.rect.bottom < CANVAS_HEIGHT:
            self.rect.y += PADDLE_SPEED + self.difficulty
        elif ball.rect.centery < self.rect.centery and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED + self.difficulty


class Ball(Scene):
    """
    Ball that bounces off of walls and paddles.
    """

    def __init__(self, x, y):
        super().__init__(left=x, top=y, width=BALL_SIZE, height=BALL_SIZE)
        self.x_vel = 0
        self.y_vel = 0
        self.set_random_direction()
        self.speed = BALL_START_SPEED

    def _on_update(self, delta_time):
        if self.rect.top <= 0 or self.rect.bottom >= CANVAS_HEIGHT:
            self.y_vel *= -1
        self.rect.move_ip(self.x_vel * self.speed, self.y_vel * self.speed)

    def set_random_direction(self):
        """
        Set a random direction for the ball.
        """
        self.x_vel = choice([-1, 1])
        self.y_vel = choice([-1, 1])

    def _on_render(self):
        pygame.draw.ellipse(self.canvas, "white", (0, 0, BALL_SIZE, BALL_SIZE))

    def reset(self):
        self.rect.center = (CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        self.set_random_direction()
        self.speed = BALL_START_SPEED
