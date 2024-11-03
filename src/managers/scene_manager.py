from .manager import Manager


class SceneManager(Manager):
    """
    Manages scenes.
    """

    default_scene = "arcade"

    def _init(self):
        from scenes import (
            Intro,
            Arcade,
            Settings,
            Clicker,
            Pong,
            ArcadeMachine,
            TicTacToe,
        )

        self.scenes = {
            "intro": Intro,
            "arcade": Arcade,
            "settings": Settings,
            "clicker": Clicker,
            "pong": Pong,
            "arcade_machine": ArcadeMachine,
            "tic_tac_toe": TicTacToe,
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
                self.current_scene.leave()
            self.current_scene = scene_class(*args, **kwargs)
            self.current_scene.enter()

    def push_scene(self, scene_name, *args, **kwargs):
        """
        Push a new scene onto the stack, keeping the current scene.
        If the new scene doesn't exist, nothing happens.
        """
        # Prevent stacking of the same scene
        if self.current_scene and self.current_scene.name == scene_name:
            return

        # Prevent pushing scenes that are already in the stack
        if scene_name in [scene.name for scene in self.scene_stack]:
            return

        scene_class = self.scenes.get(scene_name)
        if scene_class:
            if self.current_scene:
                self.current_scene.leave()
                self.scene_stack.append(self.current_scene)
            self.current_scene = scene_class(*args, **kwargs)
            self.current_scene.enter()

    def pop_scene(self):
        """
        Pop the current scene and return to the previous scene in the stack.
        If there is no previous scene, goes to the default scene.
        """
        if not self.current_scene:
            self.set_scene(self.default_scene)
            return

        if self.scene_stack:
            self.current_scene.leave()
            self.current_scene = self.scene_stack.pop()
            self.current_scene.reenter()
        elif self.current_scene.name != self.default_scene:
            self.set_scene(self.default_scene)

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
