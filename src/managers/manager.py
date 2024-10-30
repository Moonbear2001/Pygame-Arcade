from abc import ABC


class Manager(ABC):
    """
    Manages some aspect of the game's functionality. Sits above actual gameplay and
    receives all events. Enforces the singleton design pattern.
    """

    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(Manager, cls).__new__(cls)
            cls._instances[cls] = instance
            instance._initialized = False
        return cls._instances[cls]

    def __init__(self, *args, **kwargs):
        if not self._initialized:
            self._init(*args, **kwargs)
            self._initialized = True

    def _init(self, *args, **kwargs):
        """
        Only called once for instantiation. Subclasses can override to add their own
        initialization logic.
        """
        pass
