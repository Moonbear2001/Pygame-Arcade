import pygame

class SceneManager:
    """
    Manages scenes.
    Uses the singleton design pattern.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SceneManager, cls).__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        from scenes import Test, Intro, Arcade, Settings, Clicker
        self.scenes = {
            "test": Test,
            "intro": Intro,
            "arcade": Arcade,
            "settings": Settings,
            "clicker": Clicker
        }
        self.scene_stack = []
        self.current_scene = None

    def register_scene(self, scene_name, scene_class):
        """
        Add a scene to the registry.
        """
        self.scenes[scene_name] = scene_class

    def set_scene(self, scene_name, *args, **kwargs):
        """
        Set the current scene, replacing the existing scene and the whole scene stack.
        If the new scene doesn't exist, nothing happens.
        """
        scene_class = self.scenes.get(scene_name)
        if scene_class:
            if self.current_scene:
                self.current_scene.cleanup()
            self.current_scene = scene_class(*args, **kwargs)
            self.current_scene.enter()

    def push_scene(self, scene_name, *args, **kwargs):
        """
        Push a new scene onto the stack, keeping the current scene.
        If the new scene doesn't exist, nothing happens.
        """
        # Prevent stacking of the same scene by class type
        if self.current_scene and self.current_scene.name == scene_name:
            return
        scene_class = self.scenes.get(scene_name)
        if scene_class:
            if self.current_scene:
                self.scene_stack.append(self.current_scene)
            self.current_scene = scene_class(*args, **kwargs)
            self.current_scene.enter()

    def pop_scene(self):
        """
        Pop the current scene and return to the previous scene in the stack.
        If there is no previous scene, does nothing.
        """
        if self.scene_stack and self.current_scene:
            self.current_scene.cleanup()
            self.current_scene = self.scene_stack.pop()

    def update(self, delta_time):
        """
        Update the current scene.
        """
        if self.current_scene:
            self.current_scene.update(delta_time)

    def render(self):
        """
        Render the current scene and return a surface.
        """
        if self.current_scene:
            return self.current_scene.render()

    def handle_event(self, event):
        """
        Pass events to global event controls and pass events to the current scene.
        """
        self.process_global_events(event)
        if self.current_scene:
            self.current_scene.handle_event(event)

    def process_global_events(self, event):
        """
        Handle global events that are relevant to the entire game.
        This can include input handling for scene transitions or other game controls.
        """
        if event.type == pygame.KEYDOWN:
            
            # Esc go back one scene (if possible)
            if event.key == pygame.K_ESCAPE:
                self.pop_scene()

            # Example for setting a specific scene
            elif event.key == pygame.K_t:
                self.set_scene("title")
            
            # Example for pushing a settings scene
            elif event.key == pygame.K_p:
                self.push_scene("settings")

            # Example for pushing a clicker scene
            elif event.key == pygame.K_c:
                self.push_scene("clicker")
                
