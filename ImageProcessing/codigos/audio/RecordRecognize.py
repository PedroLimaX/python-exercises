# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:00:22 2023

@author: pedro
"""

import os
import serial
import time
import speech_recognition as sr

sr.__version__

#ser = serial.S
ser = serial.Serial('COM5', 9600, timeout = 1)
time.sleep(2)

r = sr.Recognizer()
harvard = sr.AudioFile('record.wav')
with harvard as source:
    audio = r.record(source)
type(audio)

print('El resultado es:')

salida = r.recognize_google(audio)
print(salida)

if salida == "light out":
    print("Apagar las luces")
    
    ser.write(b'P')
else :
    print("luces encendidas")
    ser.write(b'N')