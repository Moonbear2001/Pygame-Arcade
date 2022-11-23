import pickle
from os.path import isfile, join
from SavedGameData import SavedGameData


class SaveLoadManager:

    def __init__(self, file_extension: str, save_folder: str) -> None:
        self.file_extension = file_extension
        self.save_folder = save_folder

    def save_data(self, data: SavedGameData, file_name: str) -> None:
        """
        Serialize and save game data.
        :param data: dataclass holding game data
        :param file_name: name to save data under (pygame_template/save_data/file_name)
        :return: None
        """
        path = join(self.save_folder, file_name) + self.file_extension
        with open(path, "wb") as data_file:
            try:
                pickle.dump(data, data_file)
            except Exception as e:
                print(e)

    def load_data(self, file_name: str) -> SavedGameData:
        """
        Deserialize and load game data.
        :param file_name: name of file to be loaded
        :return: data in dataclass format
        """
        path = self.save_folder + "/" + file_name + self.file_extension

        # If the file doesn't exist, create it and return default data
        if not isfile(path):
            print("First time opening game...creating save data folder.")
            with open(path, "wb") as data_file:
                data = SavedGameData(high_score=0)
                pickle.dump(data, data_file)
                return data

        with open(path, "rb") as data_file:
            try:
                data = pickle.load(data_file)
            except FileNotFoundError as e:
                print(e)
                quit()
        return data
