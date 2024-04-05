import pyaudio
import wave

chunk = 1024  # Almacenar chunks de 1024 muestras
sample_format = pyaudio.paInt16  # 16 bits por muestra
channels = 2
fs = 44100  # Record de 44100 muestras por segundo
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()  # Crear una interface al PortAudio

print('Grabando')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # inicializar arreglos para almacenar frames

# alamacenar data en chunks para 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Detener y cerrar la transmisión 
stream.stop_stream()
stream.close()
# Terminar la interfase del PortAudio
p.terminate()

print('Finalizar grabación')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

