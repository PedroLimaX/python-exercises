# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:43:42 2022

@author: pedro
"""

from nltk.tokenize import sent_tokenize;
from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn

def synset_word(pal):
    palabra=pal.lower()
    syn = wn.synsets(palabra)[0]
    return print("Sugerencias de busqueda: ", 
                 syn.hyponyms()[0], "," , 
                 syn.hypernyms()[0], ",",
                 syn.member_holonyms())

print("Buscar : ")
palabra=input()
analizar=synset_word(palabra)
print (analizar)