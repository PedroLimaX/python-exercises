# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:27:22 2022

@author: pedro
"""

from nltk.corpus import wordnet as wn

print(wn.synsets('dog'))
print(wn.synset('car.n.02') .lemma_names('spa'))
print(wn.synset('car.n.02') .definition())
print(wn.synset('car.n.02') .examples())

motorcar=wn.synset('car.n.01')

print('---------------Muestra Hiponimos, es decir tipos de-------')
types_of_motorcar = motorcar.hyponyms()

print(types_of_motorcar)
print(sorted(lemma.name()
for synset in types_of_motorcar
for lemma in synset.lemmas()))