# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:09:20 2022

@author: erosv
"""
import re
import nltk
from nltk.tokenize import sent_tokenize;
from nltk.tokenize import word_tokenize;
from nltk.book import *

#Filtra las palabras que contienen "F"
filtrado=[word for word in text5 if not word.find("f")==-1] 
#Las ordena
ordenado=sorted(set(filtrado))
print (ordenado)

