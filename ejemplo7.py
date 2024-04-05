# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:36:08 2022

@author: pedro
"""

import nltk
import urllib.request
import re
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import StanfordPOSTagger




def tratamiento_html(text): 
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text() #obtiene el texto
    raw = re.sub('\[[^]]*\]', '', text) #elimina los corchetes
    return raw



def tokenizar(raw):
    palabras = word_tokenize(raw)
    palabras_vacias=set (stopwords.words('spanish'))
    palabras = [palabras_m.lower() for palabras_m in palabras]
    filtrado = [word for word in palabras if not word in palabras_vacias]
    final= [word for word in filtrado if word.isalnum()]
    return final


def categoria_gramatical(raw):
    tokens=word_tokenize(raw)
    tagged=nltk.pos_tag(tokens)
    return tagged
poema_ingles="Here you are, dressed up for the hight. You Knock and knock hoping to frigth. Instead I am dressed up too. I give you a fright when I Yell BOO!"
poema_espaniol= "Las noticias falsas son un negocio. Por eso cada vez más noticias falsas utilizan titulares llamativos: así se comparten más veces por las redes sociales y generan más ingresos para sus creadores. La parte negativa es que, cuanto más se comparte una noticia, más posibilidades hay de que los medios de comunicación la tomen como cierta. A continuación, un ejemplo de noticias falsas que circulan por internet: Un lobo se pasea por los vestuarios de los juegos olímpicos de invierno de Sochi En realidad no había ningún lobo en los vestuarios de Sochi. Fue una broma de la deportista Kate Hansen y el presentador Jimmy Kimmel, pero algunos medios de comunicación como la CNN cayeron en la trampa y publicaron el video como verdadero"

texto_etiquetado=categoria_gramatical(poema_espaniol)
print(texto_etiquetado)