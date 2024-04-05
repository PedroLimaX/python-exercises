# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:20:09 2022

@author: pedro
"""

from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pandas as pd
from nltk.corpus import stopwords
import os

from nltk.tokenize import sent_tokenize;

print('Escribe la ruta donde se encuentra el archivo y el nombre del archivo')
ruta=input()
archivo=open(ruta)
contenido=archivo.read()


oraciones=sent_tokenize(contenido,'spanish')
print(oraciones)
print(oraciones[0])
cant=len(oraciones)


stops=set(stopwords.words('spanish'))
text = oraciones
countvector = CountVectorizer(analyzer='word', stop_words=stops)
tfidfvector = TfidfVectorizer(analyzer = 'word', stop_words = stops)

count_wm = countvector.fit_transform(text)
tfidf_wm = tfidfvector.fit_transform(text)


count_tokens = countvector.get_feature_names()
tfidf_tokens = tfidfvector.get_feature_names()

df_countvect = pd.DataFrame(data = count_wm.toarray(), columns = count_tokens)
df_tfidfvect = pd.DataFrame(data = tfidf_wm.toarray(), columns = tfidf_tokens)


#total =count_tokens.sum()

print("Count Vectorizer\n")
print(df_countvect)

print("\nTD-IDF  Vectorizer\n")
print(df_tfidfvect)

#print("Pesado de oraciones\nSeleccionando una fila")
#print(df_tfidfvect.iloc[1])

#print("Sumando la fila")
#print(df_tfidfvect.iloc[1].sum())

pesado=[]

print("El numero de oraciones es :" + str(df_tfidfvect.shape[0]))
importante = 0
for n in range(df_tfidfvect.shape[0]):
    pesado.append(df_tfidfvect.iloc[n].sum())
    #print(df_tfidfvect.iloc[n].sum())
    if (importante < df_tfidfvect.iloc[n].sum()):
        importante = n
        
        
#Ordenar los pesos de mayor a menor
pesado.sort(reverse=True)

#obtener los primeros 5 pesos
for p in range(5):
    print(pesado[p])


#Crear el archivo

file= open("resumen.txt","w")

print("Las 5 oraciones mas importantes son: ")

#Comparar los pesados ordenados con los originales para identificar a que oracion pertenece
for i in range(5):
    for j in range(df_tfidfvect.shape[0]):
        if (pesado[i] == df_tfidfvect.iloc[j].sum()):
            #print(oraciones[j])
            print("\n\nOracion:" + str((oraciones[j])) + "\nPesado: " + str(pesado[i]))
            file.write(oraciones[j]+"\n" + os.linesep)
file.close

#print(pesado)
#print("Las oraciones mas importantes son: " + str(oraciones[importante]))
