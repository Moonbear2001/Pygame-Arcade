from .transition import Transition


class FadeFromBlack(Transition):

    def __init__(self, next_scene_name, duration):
        self.next_scene_name = next_scene_name
        self.duration = duration
