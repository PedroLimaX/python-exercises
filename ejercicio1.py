# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:04:42 2022

@author: pedro
"""

import nltk
#esto es un comentario Codigo para abrir un archivo para lectura
archivo=open('texto1.txt','r')
contenido=archivo.read()
print(contenido)
archivo.close()

#abre un archivo para escritura
archivo1=open('holamundo.txt','w')
archivo1.write('este es mi archivo nuevo creado en python el 1 de febrero de 2022')

tokens=[t for t in contenido.split()]
print(tokens)

frec_pal=nltk.FreqDist(tokens)
for pal,frec in frec_pal.items():
    print(str(pal)+": "+str(frec))
    