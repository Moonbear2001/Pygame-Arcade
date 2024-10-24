import threading
from states.state import State
from states.title import Title
from visual_elems.LoadingCircle import LoadingCircle
import Game


class Loading(State):

    def __init__(self, game):
        super().__init__(game)
        self.name = "Loading"
        self.timer = threading.Timer(1, self.go_next)
        self.timer.start()
        self.loading_circle = LoadingCircle(self, Game.canvas_width/2, self.game.Game.canvas_height * 0.65, 200, 200, center=True)

    def update(self, delta_time):
        super().update(delta_time)
        self.loading_circle.update()

    def handle_event(self, event):
        super().handle_event(event)

    def render(self):
        self.game.canvas.fill("white")
        self.game.render_text(self.game.canvas, Game.name, "roboto", "black",
                              Game.canvas_width/2, self.game.Game.canvas_height/2, size=30, center=True)
        self.loading_circle.render()
        super().render()

    def go_next(self):
        Title(self.game).enter_state()

