# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:19:12 2022

@author: pedro
"""

from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
import webbrowser

fileP="archivo.mp3"
tts = gTTS('Hola, me llamo Cortana y soy tu asistente virtual, ¿En que puedo ayudarte?', lang='es-us')
x=open(fileP, "wb+")
tts.write_to_fp(x)
x.close()
playsound(fileP)
os.remove(fileP)

r=sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    audio=r.listen(source)
    try:
        print("Escuchando...")
    except LookupError:
        print("No entiendo")
        
transcript = r.recognize_google(audio)
transcript = transcript.upper()
print('el audio dice{}',format(transcript))

#url="https://google.com/search?q="+ transcript
#webbrowser.get().open(url)