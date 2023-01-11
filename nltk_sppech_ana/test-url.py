# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:12:15 2019

@author: jk
"""

import urllib.request, urllib.parse, urllib.error
import gzip
from urllib.error import HTTPError

test_list = [['815','Democracy in America — Volume 1','Alexis de Tocqueville'],
['3296','The Confessions of St. Augustine','Bishop of Hippo Saint Augustine'],
['100','The Complete Works of William Shakespeare','William Shakespeare']]

for books in test_list:
    num= books[0]
    url = "http://www.gutenberg.org/cache/epub/"+ num + "/pg" + num + ".txt"
    url2 = "http://www.gutenberg.org/files/"+ num + "/" + num + ".txt"
    try:
        fhand = urllib.request.urlopen(url)
        print (fhand.headers)
#        fhand2 = urllib.request.urlopen(url2)
#        print (fhand2.headers)
#        for line in fhand:
#            words = line.decode().split()
#            print(words)
        raw = fhand.read()
        
        #print(raw)
        if fhand.headers['Content-Encoding'] == 'gzip':
            nom = (re.search(r'\/(\w+\.\w+$)',url)).group(1)   
            with open(nom + ".gzip", "w", encoding='utf-8') as file: 
                file.write(str(raw))
            with gzip.GzipFile(nom + ".gzip") as fin:    
                Dabytes = fin.readable()                      
#                lastring = Dabytes.decode('utf-8')
#                print(lastring)
               # print(str(raw2)) """/////////// MARCHE PAS"""
        print('************')
    except HTTPError:
        print('erreur à' + str(num))
        continue