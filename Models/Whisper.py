import whisper


class WhisperModel:
    def __init__(self, param):
        self._model = None
        self._param = param
        self.model_name = "Whisper"

    def load(self):
        self._model = whisper.load_model(self._param)

    def transcribe(self, file_path):
        return self._model.transcribe(file_path)["text"]
