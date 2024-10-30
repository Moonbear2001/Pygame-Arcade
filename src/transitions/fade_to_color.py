from .transition import Transition


class FadeToColor(Transition):
    """
    Fades the screen to a color (default black).
    """

    def __init__(self, duration=1, color="black"):
        super().__init__()
        self.duration = duration
        self.color = color
        self.current_time = 0
        self.surface.fill(color)

    def update(self, delta_time):
        self.current_time += delta_time
        fade_progress = min(1, self.current_time / self.duration)
        alpha = int(255 * fade_progress)
        self.surface.set_alpha(alpha)
        if fade_progress == 1:
            self.finished = True

    def render(self, canvas):
        canvas.blit(self.surface, (0, 0))
