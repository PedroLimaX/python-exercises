import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
#matplotlib inline
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
sampFreq, sound = wavfile.read('audio.wav')
sound.dtype, sampFreq
sound = sound / 2.0**15
length_in_s = sound.shape[0] / sampFreq
print(length_in_s)

time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s

plt.subplot(2,1,1)
plt.plot(time, sound[:,0], 'r')
plt.xlabel("tiempo, s [Canal izquierdo]")
plt.ylabel("señal, Unidades relativas")
plt.subplot(2,1,2)
plt.plot(time, sound[:,1], 'b')
plt.xlabel("tiempo, s [Canal dereho]")
plt.ylabel("señal, Unidades relativas")
plt.tight_layout()
plt.show()

