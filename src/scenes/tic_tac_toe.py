import pygame
from random import shuffle, randint

from .scene import Scene
from utilities import render_text
from constants import CANVAS_WIDTH, CANVAS_HEIGHT


# Constants
LINE_COLOR = "white"
LINE_THICKNESS = 5
BG_COLOR = "black"

TEXT_COLOR = "white"
TEXT_TOP_OFFSET = 100
TEXT_EDGE_OFFSET = 100
TEXT_SIZE = 60

CELL_SIZE = CANVAS_HEIGHT // 3
BOARD_WIDTH = CELL_SIZE * 3
BOARD_LEFT = (CANVAS_WIDTH - BOARD_WIDTH) // 2
BOARD_RIGHT = BOARD_LEFT + BOARD_WIDTH
GRID_POINTS = [
    ((BOARD_LEFT + CELL_SIZE, 0), (BOARD_LEFT + CELL_SIZE, CANVAS_HEIGHT)),
    ((BOARD_LEFT + 2 * CELL_SIZE, 0), (BOARD_LEFT + 2 * CELL_SIZE, CANVAS_HEIGHT)),
    ((BOARD_LEFT, CELL_SIZE), (BOARD_LEFT + 3 * CELL_SIZE, CELL_SIZE)),
    ((BOARD_LEFT, 2 * CELL_SIZE), (BOARD_LEFT + 3 * CELL_SIZE, 2 * CELL_SIZE)),
]


class TicTacToe(Scene):
    """
    The classic Tic-Tac-Toe game implemented using scenes.
    """

    name = "tic_tac_toe"
    custom_watched_events = {pygame.MOUSEBUTTONDOWN}

    def __init__(self):
        super().__init__(watched_events=self.custom_watched_events)
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.board_rect = pygame.Rect(BOARD_LEFT, 0, BOARD_WIDTH, CANVAS_HEIGHT)
        self.current_player = 0
        self.symbols = ["O", "X"]
        self.scores = [0, 0]
        self.move_num = 0

        # TODO: grab a saved game if there is one

    def _render_before_children(self):
        self.canvas.fill(BG_COLOR)

        # TESTING
        pygame.draw.rect(self.canvas, "pink", self.board_rect)

        render_text(
            self.canvas,
            f"Player 1 ({self.symbols[0]})",
            "roboto",
            TEXT_COLOR,
            coord=(TEXT_EDGE_OFFSET, TEXT_TOP_OFFSET),
            size=35,
        )
        render_text(
            self.canvas,
            str(self.scores[0]),
            "roboto",
            TEXT_COLOR,
            coord=(TEXT_EDGE_OFFSET, TEXT_TOP_OFFSET + 200),
            size=TEXT_SIZE,
        )
        render_text(
            self.canvas,
            f"Player 2({self.symbols[1]})",
            "roboto",
            TEXT_COLOR,
            coord=(CANVAS_WIDTH - TEXT_EDGE_OFFSET, TEXT_TOP_OFFSET),
            size=35,
        )
        render_text(
            self.canvas,
            str(self.scores[1]),
            "roboto",
            TEXT_COLOR,
            coord=(CANVAS_WIDTH - TEXT_EDGE_OFFSET, TEXT_TOP_OFFSET + 200),
            size=TEXT_SIZE,
        )
        # Draw grid
        for p1, p2 in GRID_POINTS:
            pygame.draw.line(
                self.canvas,
                LINE_COLOR,
                p1,
                p2,
                LINE_THICKNESS,
            )

        # Draw the Xs and Os
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is not None:
                    render_text(
                        self.canvas,
                        self.board[row][col],
                        "roboto",
                        TEXT_COLOR,
                        coord=(
                            BOARD_LEFT + (col * CELL_SIZE) + CELL_SIZE // 2,
                            (row * CELL_SIZE) + CELL_SIZE // 2,
                        ),
                        size=80,
                    )

    def _on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.board_rect.collidepoint(mouse_pos):
                print(mouse_pos)
                row, col = self.get_grid_pos(mouse_pos)
                print(row, col)
                # Update self.board, check for win, switch player (if necessary)
                if self.update_board(row, col):
                    self.move_num += 1
                    if self.check_for_win():
                        self.scores[self.current_player] += 1
                        self._reset_game()
                    elif self.move_num == 9:
                        self._reset_game()
                    else:
                        self.current_player = 1 - self.current_player

    def check_for_win(self):
        """
        Given a 3x3 board, check for 3 same non-empty cells.
        """
        for row in range(3):
            if (
                self.board[row][0] == self.board[row][1] == self.board[row][2]
                and self.board[row][0] is not None
            ):
                return True
        for col in range(3):
            if (
                self.board[0][col] == self.board[1][col] == self.board[2][col]
                and self.board[0][col] is not None
            ):
                return True
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2]
            and self.board[0][0] is not None
        ) or (
            self.board[0][2] == self.board[1][1] == self.board[2][0]
            and self.board[0][2] is not None
        ):
            return True
        return False

    def get_grid_pos(self, mouse_pos):
        """
        Given a mouse position as a cooordinate pair, find the cell that was clicked.
        """
        x, y = mouse_pos
        row = y // (CELL_SIZE)
        col = (x - BOARD_LEFT) // (CELL_SIZE)
        return row, col

    def update_board(self, row, col):
        """
        Update the board with a player's move.
        Return True is the move is valid and was applied, False otherwise
        """
        if self.board[row][col] is None:
            self.board[row][col] = self.symbols[self.current_player]
            return True
        return False

    def _reset_game(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        shuffle(self.symbols)
        self.current_player = randint(0, 1)
        self.move_num = 0
