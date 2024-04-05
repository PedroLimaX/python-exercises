import pyaudio
import wave
import sys

# establecer parametro entrada
chunk = 1024

# abrir el archivo a leer
wf = wave.open('audio.wav', 'rb')

# crear un objeto basado en audio
p = pyaudio.PyAudio()

# abrir la transmisión basada en el objeto forma de onda 
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# leer los datos (basado en el tamaño del parametro de entrada)
data = wf.readframes(chunk)

# reproducir el archivo
print("Reproduciendo...")
while data:
    # 
    stream.write(data)
    data = wf.readframes(chunk)

print("Reproduccion Terminada")
# cerrar y terminar
wf.close()
stream.close()    
p.terminate()
