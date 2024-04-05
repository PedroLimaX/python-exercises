# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:53:24 2022

@author: erosv
"""
import nltk
from nltk.tokenize import word_tokenize; #Sirve para dividir un texto en palabras
from nltk.book import *
#print(text4)
#print(text4.generate())
print("Numero de palabras: "+(str(len(text4))))
print("Tamano de vocabulario: " + str(len(set(text4))))
print("Listado de palabras: ")
filtro_alfnum=[word for word in text4 if word.isalnum()] #quitar simbolos
tokens_vocab=(sorted(set(filtro_alfnum))) #vocabulario
 

lista=[]
contador=0
frec_pal=nltk.FreqDist(tokens_vocab)
for pal, frec in frec_pal.items():
    #Imprime las palabras y su frecuencia en forma de listado
    #print(str(pal)+":"+str(frec)) 
    dato=str(pal)+":"+str(frec)+"\n"
    lista.append(dato)
    #Condicion para Palabras sin repeticiones
    if  frec <= 1: 
        contador+=1
        
print(str("Palabras sin repeticiones:" + str(contador))) #Palabras sin repeticiones

archivo=open('resultados.txt','w')
archivo.write("Numero de palabras: " + (str(len(text4))) + "\n" )
archivo.write("Tamano de vocabulario: " + str(len(set(text4))) + "\n" )
archivo.write("Palabras sin repeticiones: " + str(contador) + "\n" )
archivo.writelines(lista)
archivo.close()