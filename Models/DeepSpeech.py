import deepspeech
from os import path
import glob
import io
import numpy as np
from pydub import AudioSegment


class DeepSpeechModel:
    def __init__(self, param):
        self._model = None
        self._param = param
        self.model_name = "DeepSpeech"

    def load(self):
        model, scorer = self._load_model_files()
        self._model = deepspeech.Model(model)
        self._model.enableExternalScorer(scorer)

    def transcribe(self, file_path):
        audio_fragment = AudioSegment.from_mp3(file_path)
        wav_buffer = io.BytesIO()
        audio_fragment.export(wav_buffer, format="wav")
        wav_buffer.seek(0)
        buffer = np.frombuffer(wav_buffer.getvalue(), dtype=np.int16)
        return self._model.stt(buffer)

    def _load_model_files(self):
        model = glob.glob(self._param + "/*.pbmm")[0]
        scorer = glob.glob(self._param + "/*.scorer")[0]
        return model, scorer

