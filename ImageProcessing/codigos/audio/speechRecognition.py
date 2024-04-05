# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:25:41 2023

@author: pedro
"""

import speech_recognition as sr
sr.__version__

r = sr.Recognizer()
#harvard = sr.AudioFile('harvard.wav')
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
type(audio)

l = r.recognize_google(audio)

print("Texto: ", l)

l = l.split()

print("\nTexto por palabras", l)
