import pygame
from pathlib import Path

from paths import MUSIC_DIR, SOUNDS_DIR

class AudioManager:
    """
    Manages loading audio and controlling volume.
    Uses singleton design pattern.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AudioManager, cls).__new__(cls)
            cls._instance._init()
        return cls._instance
    
    def _init(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music_volume = 0.5
        self.sounds_volume = 0.5
        pygame.mixer.music.set_volume(self.music_volume)

    def set_music_volume(self, volume):
        if 0 <= volume <= 1:
            self.music_volume = volume
            pygame.mixer.music.set_volume(self.music_volume)

    def set_sounds_volume(self, volume):
        if 0 <= volume <= 1:
            self.sounds_volume = volume
            for sound in self.sounds.values():
                sound.set_volume(self.sound_volume)

    def load_sound(self, name, ext):
        """
        Load a sound effect and store it in the registry.
        If sound does not exist, does nothing.
        """
        file_path = SOUNDS_DIR / (name + "." + ext)
        if file_path.is_file():
            self.sounds[name] = pygame.mixer.Sound(file_path)

    def play_sound(self, name):
        """
        Play a sound effect by name.
        """
        if name in self.sounds:
            self.sounds[name].set_volume(self.sounds_volume)
            self.sounds[name].play()

    def play_music(self, name, ext, loops=0):
        """
        Load and play a music track.
        """
        file_path = MUSIC_DIR / (name + "." + ext)
        if file_path.is_file():
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(loops)

    def stop_all_audio(self):
        pygame.mixer.stop()
    
    

    
