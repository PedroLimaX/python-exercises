# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:58:36 2022

@author: pedro
"""

print('Escribe la ruta donde se encuentra el archivo y el nombre del archivo')
def leer (ruta):
    archivo=open(ruta)
    contenido=archivo.read()
    archivo.close()
    return contenido

open_file=leer('holaxd.txt','r')
print("Contenido del archivo: \n" + open_file)