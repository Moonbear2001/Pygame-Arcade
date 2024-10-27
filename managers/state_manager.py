class StateManager:
    """
    Manages game states.
    Uses the singleton design pattern.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StateManager, cls).__new__(cls)
            cls._instance._init()
        return cls._instance
    
    def _init(self):
        from states import Title, Loading, Settings, Clicker, Platformer, ParallaxExample, Arcade

        self.states = {
            "title": Title,
            "loading": Loading,
            "settings": Settings,
            "clicker": Clicker,
            "platformer": Platformer,
            "parallax_example": ParallaxExample,
            "arcade": Arcade
        }
        self.state_stack = []
        self.current_state = None

    def register_state(self, state_name, state_class):
        """
        Add a state to the registry.
        """
        self.states[state_name] = state_class

    def set_state(self, state_name):
        """
        Enter a new state, discarding the current state.
        If the new state doesn't exist, nothing happens.
        """
        state_class = self.states.get(state_name)
        if state_class:
            if self.current_state:
                self.current_state.cleanup()
            self.current_state = state_class() 
            self.current_state.enter()

    def push_state(self, state_name):
        """
        Enter a new state, keeping the current state.
        If the new state doesn't exist, nothing happens.
        """
        state_class = self.states.get(state_name)
        if state_class:
            if self.current_state:
                self.state_stack.append(self.current_state)
            self.current_state = state_class()
            self.current_state.enter()

    def pop_state(self):
        """
        Exit the current state.
        Falls back to the previous state in the stack if one exists. Otherwise, does nothing.
        """
        if self.state_stack and self.current_state:
            self.current_state.cleanup()
            self.current_state = self.state_stack.pop()
            self.current_state.enter()

    def handle_event(self, event):
        """
        Handle invidivual events.
        """
        if self.current_state:
            self.current_state.handle_event(event)

    def update(self, delta_time):
        """
        Update the current state.
        """
        if self.current_state:
            self.current_state.update(delta_time)

    def render(self):
        """
        Render the current state.
        """
        if self.current_state:
            return self.current_state.render()

