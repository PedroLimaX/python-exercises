# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:22:19 2023

@author: pedro
"""

import speech_recognition as sr

r = sr.Recognizer()

r.recognize_google()

harvard = sr.AudioFile('harvard.wav')

with harvard as source:
    
    audio = r.record(source)
    
type(audio)
r.recognize_google(audio)

with harvard as source:
    audio = r.record(source, duration=4)
    
    r.recognize_google(audio)
    
    
with harvard as source:
    audio1 = r.record(source, duration=4)
    audio2 = r.record(source, duration=4)

r.recognize_google(audio1)

'the stale smell of old beer lingers'

r.recognize_google(audio2)

'it takes heat to bring out the odor a cold dip'