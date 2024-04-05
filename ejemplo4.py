# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:26:26 2022

@author: pedro
"""

from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import gutenberg


corpus_ruta = 'C:/Users/pedro/OneDrive - Benemérita Universidad Autónoma de Puebla/Semestre 6/Procesamiento de Lenguaje Natural/corpus'
corpus=PlaintextCorpusReader(corpus_ruta, '.*')
print(corpus.fileids())
print(corpus.words('poema1.txt'))
print(corpus.sents('poema1.txt'))

print(gutenberg.fileids())


print(gutenberg.sents('shakespeare-caesar.txt'))


for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
    
    for fileid in corpus.fileids():
        print(corpus.words(fileid))