from states import State
from sprite.sprites import Player, HealthBar


class Platformer(State):
    """
    Simple platformer game.
    """

    def __init__(self):
        super().__init__()
        self.name = "Platformer"
        self.player1 = Player()
        self.health_bar = HealthBar()

    def update(self, delta_time):
        super().update(delta_time)
        self.player1.update(delta_time)
        self.health_bar.update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)
        self.player1.handle_event(event)

    def render(self):
        self.canvas.fill("white")
        self.canvas.blit(self.player1.render(), self.player1.rect.center)
        self.canvas.blit(self.health_bar.render(), self.health_bar.rect.center)
        
        