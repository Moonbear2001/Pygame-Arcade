import pygame
from random import shuffle

from .manager import Manager
from .save_load_manager import SaveLoadManager
from paths import MUSIC_DIR, SOUNDS_DIR
from custom_events import PLAYLIST_NEXT


class AudioManager(Manager):
    """
    Manages loading audio and controlling volume.
    """

    def _init(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music_volume = 0.5
        self.sounds_volume = 0.5
        pygame.mixer.music.set_volume(self.music_volume)
        self.playlist = []
        self.current_track_index = 0

    def handle_event(self, event):
        """
        Go to the next item in the playlist.
        """
        if event.type == PLAYLIST_NEXT:
            if self.current_track_index == len(self.playlist) - 1:
                self.current_track_index = 0
            else:
                self.current_track_index += 1
            pygame.mixer.music.set_endevent(PLAYLIST_NEXT)
            self.play_music(self.playlist[self.current_track_index])

    def save_audio_settings(self):
        SaveLoadManager().save_data(
            {"music_volume": self.music_volume, "sounds_volume": self.sounds_volume},
            "settings",
        )

    def set_music_volume(self, volume):
        if 0 <= volume <= 1:
            self.music_volume = volume
            pygame.mixer.music.set_volume(self.music_volume)
            self.save_audio_settings()

    def increase_music_volume(self, increment):
        """
        Increase the music volume by a requested increment.
        """
        self.set_music_volume(min(1, self.music_volume + increment))

    def decrease_music_volume(self, increment):
        """
        Decrease the music volume by a requested increment.
        """
        self.set_music_volume(max(0, self.music_volume - increment))

    def set_sounds_volume(self, volume):
        if 0 <= volume <= 1:
            self.sounds_volume = volume
            for sound in self.sounds.values():
                sound.set_volume(self.sounds_volume)
            self.save_audio_settings()

    def increase_sounds_volume(self, increment):
        """
        Increase the sounds volume by a requested increment.
        """
        self.set_sounds_volume(min(1, self.sounds_volume + increment))

    def decrease_sounds_volume(self, increment):
        """
        Increase the sounds volume by a requested increment.
        """
        self.set_sounds_volume(max(0, self.sounds_volume - increment))

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
        Plays music from a 'playlist'. Accepts a folder and plays music from that
        folder. No order is guaranteed.
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
