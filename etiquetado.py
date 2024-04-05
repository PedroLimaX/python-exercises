# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:17:11 2022

@author: pedro
"""

import nltk

from nltk import word_tokenize
text = word_tokenize("Hacemos retroceder el reloj, mientras perseguimos el viento")
nltk.pos_tag(text)