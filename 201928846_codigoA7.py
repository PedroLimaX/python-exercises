# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:40:07 2022

@author: erosv
"""
from nltk import word_tokenize
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
import webbrowser

def dialog_cortana(text):
    fileP="Archivo3.mp3"
    tts=gTTS (text, lang='es-us')
    x=open(fileP, "wb+")
    tts.write_to_fp(x)
    x.close()
    playsound(fileP)
    os.remove(fileP)
    print("Asistente: "+text)
    return 

def dialog_usuario():
    r = sr.Recognizer()
    mic=sr.Microphone()

    with mic as source:        
        audio=r.listen(source)        
        try:
            print("Escuchando...")
        except LookupError:
            print ("No entiendo")
    transcript = r.recognize_google(audio)
    transcript = transcript.lower()
    return transcript

def dialog_cortana2(tokens, d_c):
    texto_M=""
    for t in tokens:
        if t=="pelicula":  
            texto_M=texto_M+" "+str(t.upper())
        else:
            texto_M=texto_M+" "+t
    print ('Usuario: {}'.format(texto_M))
    dialog_cortana(d_c)
    return

def accion_web(tokens, d_c):
    texto_M=""
    for t in tokens:
        if t=="netflix":  
            texto_M=texto_M+" "+str(t.upper())
        else:
            texto_M=texto_M+" "+t
    print ('Usuario: {}'.format(texto_M))
    url='https://google.com/search?q='+texto_M
    webbrowser.get().open_new(url)
    dialog_cortana(d_c)
    return

tx1='Hola soy tu asistente virtual, mi nombre es Cortana, en que te puedo ayudar?'
tx2='Puedo buscar en amazon prime o en netflix'
tx3='Listo, fue un placer ayudarte'
dialog_cortana(tx1)
fin=0
while fin ==0 : 
    r_usuario=dialog_usuario()
    tokens = word_tokenize(r_usuario)
    print(tokens)

    for a in tokens:
        if a=="netflix":
            oracion=2
        elif a=="pelicula":
            oracion=1
    
    if (oracion==1):
        dialog_cortana2(tokens, tx2)
    
    elif (oracion==2):
        accion_web(tokens, tx3)
        fin=1;
       
       
    
    