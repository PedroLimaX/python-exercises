# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 14:22:26 2022

@author: pedro
"""

import urllib.request
import re
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords

def tratamiento_html(text):
    soup = BeautifulSoup(text,"html.parser")
    text=soup.get_text()
    raw=re.sub('\[[^]]*\]','', text)
    return raw
def tokenizar(raw):
    palabras=word_tokenize(raw)
    palabras_vacias=set (stopwords.words('spanish'))
    palabras=[palabras_m.lower() for palabras_m in palabras]
    filtrado = [word for word in palabras if not word in palabras_vacias]
    final = [word for word in filtrado if word.isalnum()]
    return final

url ="https://www.elsoldepuebla.com.mx/local/llegaran-100-custodios-mas-al-penal-de-san-miguel-7866169.html"
webScrapping = urllib.request.urlopen(url)
html = webScrapping.read()

raw = tratamiento_html(html)
tokens = str(tokenizar(raw))
print(tokens)