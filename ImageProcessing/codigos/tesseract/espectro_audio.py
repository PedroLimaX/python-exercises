#Ejemplo obtenido del siguiente enlace verificar 
# https://learnpython.com/blog/plot-waveform-in-python/
#nota: LRC 17-04-2023
# https://noeliagorod.com/2021/08/25/audio-data-analysis-using-deep-learning-with-python/



import wave
import numpy as np
import matplotlib.pyplot as plt

wav_obj = wave.open('audio.wav', 'rb')
sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
t_audio = n_samples/sample_freq
n_channels = wav_obj.getnchannels()
signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
l_channel = signal_array[0::2]
r_channel = signal_array[1::2]
times = np.linspace(0, n_samples/sample_freq, num=n_samples)

#-----esta parte sirve para graficar en el dominio del tiempo----
plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Left Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()


# Esta parte sirve para graficar en el dominio de la frecuencia----
plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()
