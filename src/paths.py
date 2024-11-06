"""
Contains constants that show provide paths to useful locations in the project.
"""

from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

# Assets
ASSETS_DIR = ROOT_DIR / "assets"
SPRITESHEETS_DIR = ASSETS_DIR / "spritesheets"
IMAGES_DIR = ASSETS_DIR / "images"
SOUNDS_DIR = ASSETS_DIR / "sounds"
FONTS_DIR = ASSETS_DIR / "fonts"
MUSIC_DIR = ASSETS_DIR / "music"
PARALLAX_DIR = ASSETS_DIR / "images" / "parallax"

# Saving
SAVE_DIR = ROOT_DIR / "save"
SAVED_DATA_DIR = SAVE_DIR / "data"
SAVE_DATA_TEMPLATES_DIR = SAVE_DIR / "data_templates"
