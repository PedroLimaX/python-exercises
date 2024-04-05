import pyaudio      
import struct       #para convertir el dato binario dela señal a aentero
import matplotlib.pyplot as plt     #despliegue de la señal de audio

import numpy as np
import time

#funcion
def plot_setup():
    # crear grafica
    fig=plt.figure()
    ax=fig.add_subplot(111)

    # variable para graficación
    x = np.arange(0, 2 * CHUNK, 2)

    # crear datos aleatorio
    line, = ax.plot(x, [128 for i in range(2048)], '-')

    # formato de la gráfica
    ax.set_title('Forma de onda audio')
    ax.set_xlabel('Muestras')
    ax.set_ylabel('volumen')
    ax.set_ylim(0, 255)
    ax.set_xlim(0, 2 * CHUNK)
    plt.xticks([0, CHUNK, 2 * CHUNK])
    plt.yticks([0, 128, 255])
    # mostrar la grafica
    plt.show(block=False)
    return fig, line

def measure():
    # datos binarios
    data = stream.read(CHUNK)  

    # convertir data a enteros, hacer un np array, con un offset de 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    # crear un arreglo np array y offset de 128
    data_np = np.array(data_int, dtype='b')[::2]
    data_np = [i+127 for i in data_np]

    line.set_ydata(data_np)
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
    except:
        return 0

# constants
CHUNK = 1024 * 2             # muestras por cuadro
FORMAT = pyaudio.paInt16     # formato audio
CHANNELS = 1                 # canal simple para microfono
RATE = 44100                 # muestras por segundo

# pyaudio instancia de clase
mic = pyaudio.PyAudio()

# usar el microfono para captar la señal
stream = mic.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

if __name__=="__main__":
    fig, line=plot_setup()
    while True:
        m=measure()
        if m==0:
            break

