# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:49:34 2022

@author: pedro
"""
import re
import nltk
from nltk.tokenize import sent_tokenize;
from nltk.tokenize import word_tokenize;
from nltk.book import *

genesis=text3.generate()
palabras=word_tokenize(genesis,'spanish')
#print(palabras)
patron= r'\b\w{3,3}\b' #se usa para definir el patron del rango {min, max}
pal_3 = re.findall(patron,genesis)

print("------------Frecuencia de palabras de 3 letras---------------")
frec_pal=nltk.FreqDist(pal_3)
for pal,frec in frec_pal.most_common():
    print(str(pal)+": "+str(frec))
