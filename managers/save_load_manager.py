import json
from pathlib import Path

from paths import SAVED_DATA_DIR, SAVE_DATA_TEMPLATES_DIR


class SaveLoadManager:
    """
    Manages the loading a saving of data to json files.

    Uses the singleton design pattern, a single instance of this manager can be used anywhere in the project.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SaveLoadManager, cls).__new__(cls)
        return cls._instance

    def save_data(self, data: dict, file_name: str) -> None:
        """
        Save game data, create the file if it doesn't already exist.
        """
        file_path = SAVED_DATA_DIR / (file_name + ".json")
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        
    def load_data(self, file_name: str) -> dict:
        """
        If the saved data exists, load the JSON and return it as a dictionary. 
        Otherwise load the template and return the default data.
        """
        saved_data = Path(SAVED_DATA_DIR / (file_name + ".json"))
        if saved_data.is_file():
            with open(saved_data, 'r') as file:
                return json.load(file)
        else:
            return json.load(SAVE_DATA_TEMPLATES_DIR / (file_name + "json"))
