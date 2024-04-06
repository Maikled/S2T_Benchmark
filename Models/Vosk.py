import json
import vosk
from pydub import AudioSegment


class VoskModel:
    def __init__(self, param):
        self._model = None
        self._param = param
        self.model_name = "Vosk"

    def load(self):
        self._model = vosk.Model(self._param)

    def transcribe(self, file_path):
        audio_fragment = AudioSegment.from_mp3(file_path)
        audio_fragment = audio_fragment.set_frame_rate(8000)
        rec = vosk.KaldiRecognizer(self._model, 8000)
        rec.AcceptWaveform(audio_fragment.raw_data)
        result = rec.Result()
        return json.loads(result)["text"]
