# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:22:29 2023

@author: pedro
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile



#matplotlib inline

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
sampFreq, sound = wavfile.read('audio01.wav')
sound.dtype, sampFreq
sound = sound / 2.0**15
length_in_s = sound.shape[0] / sampFreq
print('Duracion Audio 1:', length_in_s)
time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s


sampFreq2, sound2 = wavfile.read('audio02.wav')
sound2.dtype, sampFreq2
sound2 = sound2 / 2.0**15
length_in_s2 = sound2.shape[0] / sampFreq2
print('Duracion Audio 2:', length_in_s2)
time2 = np.arange(sound2.shape[0]) / sound2.shape[0] * length_in_s2

#-----------------------------Audio 1-------------------------------------
#Grafica para la señal del canal izquierdo
plt.subplot(2,1,1)
plt.gca().set_title('AUDIO 1')
plt.plot(time, sound[:,0], 'r')
plt.xlabel("tiempo, s [Canal izquierdo]")
plt.ylabel("señal, Unidades relativas")

#Grafica para la señal del canal derecho
plt.subplot(2,1,2)
plt.plot(time, sound[:,1], 'b')
plt.xlabel("tiempo, s [Canal dereho]")
plt.ylabel("señal, Unidades relativas")
plt.tight_layout()
plt.show()


#-----------------------------Audio 2-------------------------------------
#Grafica para la señal del canal izquierdo
plt.subplot(2,1,1)
plt.gca().set_title('AUDIO 2')
plt.plot(time2, sound2[:,0], 'r')
plt.xlabel("tiempo, s [Canal izquierdo]")
plt.ylabel("señal, Unidades relativas")

#Grafica para la señal del canal derecho
plt.subplot(2,1,2)
plt.plot(time2, sound2[:,1], 'b')
plt.xlabel("tiempo, s [Canal dereho]")
plt.ylabel("señal, Unidades relativas")
plt.tight_layout()
plt.show()




#---------------------------------Audio Nuevo------------------------------
import wave

infiles = ["audio01.wav", "audio02.wav"]
outfile = "audioNuevo.wav"

data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
    
output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()


#Nuevo Audio Señales
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
sampFreqNew, soundNew = wavfile.read('audioNuevo.wav')
soundNew.dtype, sampFreqNew
soundNew = soundNew / 2.0**15
length_in_sNew = soundNew.shape[0] / sampFreqNew
print('Duracion Audio Nuevo:', length_in_sNew)
timeNew = np.arange(soundNew.shape[0]) / soundNew.shape[0] * length_in_sNew


#-----------------------------AUDIO NUEVO-------------------------------------
#Grafica para la señal del canal izquierdo
plt.subplot(2,1,1)
plt.gca().set_title('AUDIO NUEVO')
plt.plot(timeNew, soundNew[:,0], 'r')
plt.xlabel("tiempo, s [Canal izquierdo]")
plt.ylabel("señal, Unidades relativas")

#Grafica para la señal del canal derecho
plt.subplot(2,1,2)
plt.plot(timeNew, soundNew[:,1], 'b')
plt.xlabel("tiempo, s [Canal dereho]")
plt.ylabel("señal, Unidades relativas")
plt.tight_layout()
plt.show()


#--------------------------------------ESPECTRO DE FRECUENCIAS-------------------------------

#-----------------------------------AUDIO 1----------------------------------------------

wav_obj = wave.open('audio01.wav', 'rb')
sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
t_audio = n_samples/sample_freq
n_channels = wav_obj.getnchannels()
signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
l_channel = signal_array[0::2]
r_channel = signal_array[1::2]


plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel AUDIO 1')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()

#-----------------------------------AUDIO 2---------------------------------------------
wav_obj2 = wave.open('audio02.wav', 'rb')
sample_freq2 = wav_obj2.getframerate()
n_samples2 = wav_obj2.getnframes()
t_audio2 = n_samples2/sample_freq2
n_channels2 = wav_obj2.getnchannels()
signal_wave2 = wav_obj2.readframes(n_samples2)
signal_array2 = np.frombuffer(signal_wave, dtype=np.int16)
l_channel2 = signal_array[0::2]
r_channel2 = signal_array[1::2]


plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel AUDIO 2')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio2)
plt.colorbar()
plt.show()

#-----------------------------------AUDIO NUEVO---------------------------------------------
wav_objNew = wave.open('audioNuevo.wav', 'rb')
sample_freqNew = wav_objNew.getframerate()
n_samplesNew = wav_objNew.getnframes()
t_audioNew = n_samplesNew/sample_freqNew
n_channelsNew = wav_objNew.getnchannels()
signal_waveNew = wav_objNew.readframes(n_samplesNew)
signal_arrayNew = np.frombuffer(signal_wave, dtype=np.int16)
l_channelNew = signal_array[0::2]
r_channelNew = signal_array[1::2]


plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel AUDIO NUEVO')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audioNew)
plt.colorbar()
plt.show()