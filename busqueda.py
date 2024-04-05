# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:11:56 2022

@author: pedro
"""

from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pandas as pd
from nltk.corpus import stopwords

from nltk.tokenize import sent_tokenize
from scipy import spatial

def abrir_archivo():
    archivo=open('time//TIME.ALL','r')
    contenido=archivo.read()
    archivo.close()
    return contenido

def vectorial(documentos):
    stops=set(stopwords.words('english'))
    tfidfvector = TfidfVectorizer(analyzer = 'word', stop_words = stops)
    tfidf_wm = tfidfvector.fit_transform(documentos)
    tfidf_tokens = tfidfvector.get_feature_names()
    df_tfidfvect = pd.DataFrame(data = tfidf_wm.toarray(), columns = tfidf_tokens)
    return df_tfidfvect

def coseno(vect,indice1,indice2):
   
    List1 = vect.iloc[indice1]
    List2 = vect.iloc[indice2]
    similitud = 1 - spatial.distance.cosine(List1, List2)
    return similitud


documento = abrir_archivo()
print(documento)


docs = documento.split('*TEXT')
print(docs)

vectores= vectorial(docs)
print(vectores)


simil = coseno(vectores,424,1)
print(simil)