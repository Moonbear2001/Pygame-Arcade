from states.state import State
from sprites.Player import Player


class Platformer(State):
    """
    Simple platformer game.
    """

    def __init__(self, game):
        super().__init__(game)
        self.name = "Platformer"
        self.player1 = Player(self.game)

    def update(self, delta_time):
        super().update(delta_time)
        self.player1.update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)
        self.player1.handle_event(event)

    def render(self):
        self.game.canvas.fill("white")
        self.player1.render()
        super().render()
