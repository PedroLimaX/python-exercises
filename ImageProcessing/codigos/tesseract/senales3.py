#https://klyshko.github.io/teaching/2019-02-22-teaching

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

fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)

fft_spectrum_abs = np.abs(fft_spectrum)
plt.plot(freq, fft_spectrum_abs)
plt.xlabel("frequencia, Hz")
plt.ylabel("Amplitud, unidades")
plt.show()


