import json
from pathlib import Path

from .manager import Manager
from paths import SAVED_DATA_DIR, SAVE_DATA_TEMPLATES_DIR


class SaveLoadManager(Manager):
    """
    Manages the loading and saving of data to json files.

    You can define a "template" or what the default data should look like if none
    exists in the "save/data_templates" directory. If there is no existing saved data
    and the template exists, that data will be provided.
    """

    def save_data(self, data: dict, file_name: str) -> None:
        """
        Save game data, create the file if it doesn't already exist.
        """
        file_path = SAVED_DATA_DIR / (file_name + ".json")
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self, file_name: str) -> dict:
        """
        Load saved data, if it exists.
        """
        saved_data = Path(SAVED_DATA_DIR / (file_name + ".json"))
        data_template_file = SAVE_DATA_TEMPLATES_DIR / (file_name + "_template.json")

        # Load the saved data
        if saved_data.is_file():
            file_path = saved_data

        # Load the data template
        elif data_template_file.is_file():
            file_path = data_template_file

        # No saved data or template, there is some error, return an empty dict
        else:
            return {}

        with open(file_path, "r") as file:
            data = json.load(file)
        return data
