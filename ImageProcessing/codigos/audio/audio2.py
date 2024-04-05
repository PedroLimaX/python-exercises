#leer un archivo de audio

import pyaudio
import wave

objeto = wave.open('audio.wav')
print("Nº de Canales", objeto.getnchannels())
