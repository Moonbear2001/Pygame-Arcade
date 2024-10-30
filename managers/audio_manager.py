import pygame
from pathlib import Path
from random import shuffle

from paths import MUSIC_DIR, SOUNDS_DIR
from custom_events import PLAYLIST_NEXT


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
        self.playlist = []
        self.current_track_index = 0

    def set_music_volume(self, volume):
        if 0 <= volume <= 1:
            self.music_volume = volume
            pygame.mixer.music.set_volume(self.music_volume)

    def increase_music_volume(self, increment):
        """
        Increase the music volume by a requested increment.
        """
        self.set_music_volume(min(1, self.music_volume + increment))
        print(f"music vol: {self.music_volume}")

    def decrease_music_volume(self, increment):
        """
        Decrease the music volume by a requested increment.
        """
        print("decrease calc: ", self.music_volume - increment)
        self.set_music_volume(max(0, self.music_volume - increment))
        print(f"music vol: {self.music_volume}")

    def set_sounds_volume(self, volume):
        if 0 <= volume <= 1:
            self.sounds_volume = volume
            for sound in self.sounds.values():
                sound.set_volume(self.sounds_volume)

    def increase_sounds_volume(self, increment):
        """
        Increase the sounds volume by a requested increment.
        """
        self.set_sounds_volume(min(1, self.sounds_volume + increment))
        print(f"sfx vol: {self.sounds_volume}")

    def decrease_sounds_volume(self, increment):
        """
        Increase the sounds volume by a requested increment.
        """
        self.set_sounds_volume(max(0, self.sounds_volume - increment))
        print(f"sfx vol: {self.sounds_volume}")

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

    def play_music(self, file_path, loops=0):
        """
        Load and play a music track provided a file path starting at MUSIC_DIR.
        """
        full_path = MUSIC_DIR / file_path
        if full_path.is_file():
            pygame.mixer.music.load(full_path)
            pygame.mixer.music.set_volume(self.music_volume)
            pygame.mixer.music.play(loops)

    def play_playlist(self, folder_name):
        """
        Plays music from a 'playlist'. Accepts a folder and plays music from that folder. No order is guaranteed.
        Play the full playlist and then restart the playlist.
        """
        folder_path = MUSIC_DIR / folder_name
        if folder_path.is_dir():
            self.playlist = [folder_path / file for file in folder_path.iterdir()]
            if self.playlist:
                shuffle(self.playlist)
                self.current_track_index = 0
                pygame.mixer.music.set_endevent(PLAYLIST_NEXT)
                self.play_music(self.playlist[0])

    def stop_all_audio(self):
        pygame.mixer.stop()

    def handle_event(self, event):
        if event.type == PLAYLIST_NEXT:
            print("playlist next")
            if self.current_track_index == len(self.playlist) - 1:
                print("restart")
                self.current_track_index = 0
            else:
                print("next song")
                self.current_track_index += 1
            pygame.mixer.music.set_endevent(PLAYLIST_NEXT)
            self.play_music(self.playlist[self.current_track_index])
