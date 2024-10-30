from .transition import Transition


class FadeToBlack(Transition):
    """
    Fades the screen to black.
    """

    def __init__(self, next_scene_name, duration=1):
        super().__init__(next_scene_name)
        self.duration = duration
        self.current_time = 0
        self.surface.fill("black")

    def update(self, delta_time):
        self.current_time += delta_time
        fade_progress = min(1, self.current_time / self.duration)
        alpha = int(255 * fade_progress)
        self.surface.set_alpha(alpha)
        if fade_progress == 1:
            self.finished = True

    def render(self, canvas):
        canvas.blit(self.surface, (0, 0))
