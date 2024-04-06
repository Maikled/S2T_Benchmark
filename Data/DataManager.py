from Data.DataSpace import ObjectData
from os import path
import pandas as pd


class CorpusManager():
    def __init__(self, path_to_data):
        self.path_to_audio_folder = path.join(path_to_data, "clips")
        self.path_to_target_text_file = path.join(path_to_data, "other.tsv")
        self._path_to_data = path_to_data
        self._data = []

    def load_data(self):
        file_data = pd.read_csv(self.path_to_target_text_file, sep='\t')
        for audio_path, target_text in zip(file_data["path"], file_data["sentence"]):
            if path.exists(path.join(self.path_to_audio_folder, audio_path)):
                self._data.append(ObjectData(audio_path, target_text))

        return self._data

    def save_results_data(self, save_path, string_data):
        with open(save_path, "a", encoding="utf8") as file:
            file.write(string_data + '\n')
