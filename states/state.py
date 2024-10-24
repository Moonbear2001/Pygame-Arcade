from pygame.locals import QUIT
import pygame


class State:
    """
    A state that the game can be in (ie. menu, paused, looking at map, gaemplay, etc). A state is reponsible for passing events, updating, and drawing each of"""

    def __init__(self, game):
        self.name = ""
        self.game = game
        self.prev_state = None

    def update(self, delta_time):
        pass

    def render(self):

        # Print game info
        fps = f"FPS: {self.game.fps}"
        self.game.render_text(self.game.canvas, fps, "roboto", "blue",
                              0.01 * self.game.canvas_width, 0.03 * self.game.canvas_height, size=20, center=False)
        stack = "State stack: "
        for state in self.game.state_stack:
            stack += state.name + ", "
        self.game.render_text(self.game.canvas, stack, "roboto", "blue",
                              0.01 * self.game.canvas_width, 0.08 * self.game.canvas_height, size=20, center=False)

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        else:
            self.prev_state = None
        self.game.state_stack.append(self)

    def handle_event(self, event):

        # Quit gracefully
        if event.type == pygame.QUIT:
            self.exit_state()
            self.game.game_quit()

        # Press T to return to title screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                self.exit_state()
            if event.key == pygame.K_ESCAPE:
                self.exit_state()
                self.game.game_quit()

    def exit_state(self):
        self.game.state_stack.pop()
