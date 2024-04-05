import pyaudio
import wave

senal = wave.open("audio.wav")
pa = pyaudio.PyAudio()
pa.get_default_host_api_info()

for id in range(pa.get_host_api_count()):
    print(pa.get_host_api_info_by_index(id))

pa.get_default_output_device_info()


print("numero de canales",senal.getnchannels())
print("sample width", senal.getsampwidth())
print("tasa de frames",senal.getframerate())
print("numero de frames",senal.getnframes())
print("parametros",senal.getparams())
