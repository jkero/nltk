# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:10:21 2019

@author: jk
"""

#chap3_nlp

from __future__ import division
import nltk, re, pprint
from nltk import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from urllib.request import urlopen
#url = "http://www.gutenberg.org/files/6762/6762.txt"
url="http://www.gutenberg.org/cache/epub/11/pg11.txt"
stop_words = ['\r', '\n']

def clean_data(tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tokens):
        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token)
    return cleaned_tokens


raw = urlopen(url).read()
print(raw)
#print(raw[1:].decode('utf-8'))
#print(type(raw))
#n = str(raw).replace('\\r', ' ')
#z = n.replace('\\n', ' ')
#print(z)
#s = 'CHAPTER I'

#a = bytearray(s,'utf-8')
#
#s2= 'End of the Project Gutenberg EBook of Politics, by Aristotle'
#b = bytearray(s2,'utf-8')
#
#content = raw[raw.rfind(a):raw.rfind(b)]
#
#
#print(str(content).replace('\r\n',''))

#tokens = word_tokenize(str(z))
#print(tokens)
#len(tokens)
#text = nltk.Text(tokens)
#print(text.concordance_list('slave'))


#cleaned_tokens = clean_data(tokens, stop_words = stop_words)
#print(cleaned_tokens)
#text2 = nltk.Text(cleaned_tokens)
#text2.concordance('slavery')
