"""
Contains constants that show provide paths to useful locations in the project.
"""

from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
SPRITESHEETS_DIR = ROOT_DIR / "assets" / "spritesheets"
IMAGES_DIR = ROOT_DIR / "assets" / "images"
SOUNDS_DIR = ROOT_DIR / "assets" / "sounds"
FONTS_DIR = ROOT_DIR / "assets" / "fonts"
MUSIC_DIR = ROOT_DIR / "assets" / "music"
PARALLAX_DIR = ROOT_DIR / "assets" / "images" / "parallax_backgrounds"
SAVED_DATA_DIR = ROOT_DIR / "save" / "data"
SAVE_DATA_TEMPLATES_DIR = ROOT_DIR / "save" / "data_templates"