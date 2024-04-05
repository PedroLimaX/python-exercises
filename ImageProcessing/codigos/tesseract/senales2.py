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
signal = sound[:,0]
time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s


plt.plot(time[6000:7000], signal[6000:7000])
plt.xlabel("tiempo, s")
plt.ylabel("Senal, Unidades relativas")
plt.show()

