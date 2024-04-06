import Benchmark
from Models.Whisper import WhisperModel
from Models.Vosk import VoskModel
from Models.DeepSpeech import DeepSpeechModel
from Data.DataManager import CorpusManager


path_to_dataset = r"C:\Users\zyuly\Downloads\cv-corpus-17.0-delta-2024-03-15\ru"

param_path_to_deepspeech_model = r"C:\Users\zyuly\Downloads\deepspech_files"
param_path_to_vosk_model = r"C:\Users\zyuly\Downloads\vosk-model-ru-0.42"
param_whisper_model = "medium"

# model = DeepSpeechModel(param_path_to_deepspeech_model)
# model = VoskModel(param_path_to_vosk_model)
model = WhisperModel(param_whisper_model)

data_manager = CorpusManager(path_to_dataset)

Benchmark.run(model, data_manager)
