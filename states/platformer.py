from states.state import State
from sprites.Player import Player


class Platformer(State):

    def __init__(self, game):
        super().__init__(game)
        self.name = "Platformer"
        self.player1 = Player(self.game, self.game.example_sprite_sheet)

    def update(self):
        super().update()
        self.player1.update()

    def handle_event(self, event):
        super().handle_event(event)
        self.player1.handle_event(event)

    def render(self):
        self.game.canvas.fill(self.game.colors["white"])
        self.player1.render()
        super().render()
