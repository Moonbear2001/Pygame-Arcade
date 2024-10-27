from .transition import Transition

class FadeFromBlack(Transition):

    def __init__(self, next_state_name, duration):
        self.next_state_name = next_state_name
        self.duration = duration