# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:58:38 2022

@author: pedro
"""

from nltk.tokenize import sent_tokenize;
from nltk.tokenize import word_tokenize;
from nltk.corpus import stopwords;
texto="Las noticias falsas son un negocio. Por eso cada vez más noticias falsas utilizan titulares llamativos: así se comparten más veces por las redes sociales y generan más ingresos para sus creadores. La parte negativa es que, cuanto más se comparte una noticia, más posibilidades hay de que los medios de comunicación la tomen como cierta. A continuación, un ejemplo de noticias falsas que circulan por internet: Un lobo se pasea por los vestuarios de los juegos olímpicos de invierno de Sochi En realidad no había ningún lobo en los vestuarios de Sochi. Fue una broma de la deportista Kate Hansen y el presentador Jimmy Kimmel, pero algunos medios de comunicación como la CNN cayeron en la trampa y publicaron el video como verdadero"
print("------------------------texto original-----------------------------")
print(texto)
print("------------------------texto en oraciones-----------------------------")
oraciones=sent_tokenize(texto,'spanish')
print(oraciones)
print("------------------------texto en palabras-----------------------------")
palabras=word_tokenize(texto)
print(palabras)
print("------------------------stopwords espanol (palabras vacias)-----------------------------")
palabras_vacias=set(stopwords.words('spanish'))
print(palabras_vacias)
print("------------------------tokens en minusculas-----------------------------")
palabras=[palabras_m.lower() for palabras_m in palabras] #sirve para poner todo en minuscula
print(palabras)
print("------------------------Palabras de contenido-----------------------------") 
filtrado=[word for word in palabras if not word in palabras_vacias] #sirve para quitar palabras vacias
print(filtrado)

final=[word for word in filtrado if word.isalnum()] #sirve para quitar signos de puntuacion
print(final)