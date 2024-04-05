import pyaudio
import wave
import sys

class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ iniciar tranmisión de audio """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Reproducir archivo completo """
        print('Reproduciendo audio...')
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ terminar reproducción """ 
        print('Reproduccion Terminada')
        self.stream.close()
        self.p.terminate()

# Reproducción de audio
a = AudioFile("audio.wav")
a.play()
a.close()
