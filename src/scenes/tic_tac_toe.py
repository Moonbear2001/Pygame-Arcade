import pygame

from .scene import Scene
from utilities import render_text
from constants import CANVAS_WIDTH, CANVAS_HEIGHT


# Constants
LINE_COLOR = "white"
LINE_THICKNESS = 5
BG_COLOR = "black"

TEXT_COLOR = "white"
TEXT_TOP_OFFSET = 100
TEXT_EDGE_OFFSET = 200
TEXT_SIZE = 60

CELL_SIZE = CANVAS_HEIGHT // 3
LEFT_OFFSET = (CANVAS_WIDTH - 3 * CELL_SIZE) // 2
GRID_POINTS = [
    ((LEFT_OFFSET + CELL_SIZE, 0), (LEFT_OFFSET + CELL_SIZE, CANVAS_HEIGHT)),
    ((LEFT_OFFSET + 2 * CELL_SIZE, 0), (LEFT_OFFSET + 2 * CELL_SIZE, CANVAS_HEIGHT)),
    ((LEFT_OFFSET, CELL_SIZE), (LEFT_OFFSET + 3 * CELL_SIZE, CELL_SIZE)),
    ((LEFT_OFFSET, 2 * CELL_SIZE), (LEFT_OFFSET + 3 * CELL_SIZE, 2 * CELL_SIZE)),
]


class TicTacToe(Scene):
    """
    The classic Tic-Tac-Toe game implemented using scenes.
    """

    name = "tic_tac_toe"
    custom_watched_events = {pygame.MOUSEBUTTONDOWN}

    def __init__(self):
        super().__init__(watched_events=self.custom_watched_events)
        self.left_player_score = 0
        self.right_player_score = 0
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_player = "X"
        # TODO: grab a saved game if there is one

    def _on_render(self):
        self.canvas.fill(BG_COLOR)
        render_text(
            self.canvas,
            str(self.left_player_score),
            "roboto",
            TEXT_COLOR,
            coord=(TEXT_EDGE_OFFSET, TEXT_TOP_OFFSET),
            size=TEXT_SIZE,
        )
        render_text(
            self.canvas,
            str(self.right_player_score),
            "roboto",
            TEXT_COLOR,
            coord=(CANVAS_WIDTH - TEXT_EDGE_OFFSET, TEXT_TOP_OFFSET),
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
                            (col * CELL_SIZE) + CELL_SIZE // 2,
                            (row * CELL_SIZE) + CELL_SIZE // 2,
                        ),
                        size=30,
                    )

    def _on_event(self, event):
        print(type(event))

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row, col = self.get_grid_pos(mouse_pos)

            # Update self.board, check for win, switch player (if necessary)
            if self.update_board(row, col):
                if self.check_for_win():
                    print("win")
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"

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
        row = y // (CANVAS_HEIGHT // 3)
        col = x // (CANVAS_HEIGHT // 3)
        return row, col

    def update_board(self, row, col):
        """
        Update the board with a player's move.
        Return True is the move is valid and was applied, False otherwise
        """
        print("row, col")
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            return True
        return False
