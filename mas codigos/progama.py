# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:48:02 2022

@author: erosv
"""
from nltk.tokenize import sent_tokenize;#Sirve para dividir un texto en oraciones
from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn

def abrir_archivo(nombre, modo):
    archivo=open(nombre, modo)
    contenido=archivo.read()
    archivo.close()
    return contenido

def seleccion_lista(numero, lista):
    oraciones=lista[int(numero)]
    return oraciones 

def mostrar_sin(sust):
    sinonimos = [] 
    for syn in wn.synsets(str(sust.lower())): 
        for l in syn.lemmas(): 
            sinonimos.append(l.name()) 
    return sinonimos

def sustantivos(sus, sin, pal):
    for x in pal:
        palabra=x.lower()
        if palabra==sus.lower():
            pal[pal.index(x)]=sin
    return pal

def tokenizar(oracion):
    palabras = word_tokenize(oracion)
    palabras_vacias=set (stopwords.words('english'))
    palabras = [palabras_m.lower() for palabras_m in palabras]
    filtrado = [word for word in palabras if not word in palabras_vacias]
    final= [word for word in filtrado if word.isalnum()]
    return final

def select_token(selected, pal):
    for x in pal:
        palabra=x.lower()
        if palabra==selected.lower():
            syn=wn.synsets(palabra)[0]
            antonyms = []
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
    return print("Palabra seleccionada: ",syn.name(),
                         "\nHiperonimos: ", syn.hypernyms() ,
                         "\nHiponimos: ", syn.hyponyms(), 
                         "\nRaiz: ", syn.root_hypernyms(),
                         "\nMeronimos:", syn.part_meronyms(),
                         "\nHolonimos: ", syn.member_holonyms(),
                         "\nConsecutivos logicos:", syn._shortest_hypernym_paths(syn),
                         "\nAntonimos:", antonyms
                         )



print("Ingresa la direccion del documento \n")
D=input()#pedir direccion 
texto=abrir_archivo(D,'r')
print(texto)



oraciones=sent_tokenize(texto,"english")
#print(type(oraciones))
#print(len(oraciones))
oraciones.insert(0, "")


print("\n Selecciona la oracion de la posicion 1 a "+ str( len(oraciones)) + "\n" )
N=input()#pedir direccion 
oracion=seleccion_lista(N, oraciones)

print("\n"+oracion+"\n")
palabras=word_tokenize(oracion,"english")
#print(palabras)
#print(type(palabras))


print("\n Coloque los sinonimos de 3 sustantivos a cambiar en la oracion \n")
print("\n Sustantivo 1 \n")
sus1=input() #pedir sustantivo
print("\n Posibles sinonimos: \n")
print(mostrar_sin(sus1))
print("\n Sinonimo a elegir")
sin1=input()#pedir  sinonimo 1

print("\n Sustantivo 2")
sus2=input()
print("\n Posibles sinonimos: \n")
print(mostrar_sin(sus2))
print("\n Sinonimo a elegir \n")
sin2=input()#pedir sinonimo 2

print("\n Sustantivo 3 \n")
sus3=input()
print("\n Posibles sinonimos: \n")
print(mostrar_sin(sus3))
print("\n Sinonimo a elegir \n")
sin3=input()#pedir sinonimo 3

oracion_1=sustantivos(sus1, sin1, palabras)
oracion_2=sustantivos(sus2, sin2, oracion_1)
oracion_3=sustantivos(sus3, sin3, oracion_2)

print("\n" , oracion_3, "\n")

#-------- Mostrar oracion por tokens, escoger uno y obtener sus hiponimos,
#---------hiperonimos, meronimos, holonimos, consegutivos logicos y antonimos
tokens=tokenizar(oracion)
print(tokens)

print("Escribe la palabra que deseas analizar:\n")
selected=input()
analizar=select_token(selected,palabras)
print (analizar)




