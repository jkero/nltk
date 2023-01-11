# je veux un algorithme pour trier une liste d'enr de plusieurs champs
# le tri doit se faire sur 3 niveaux adresse-num-de tel-nom
# et une variation du critere de tri a souhait.
# >>> import csv
# >>> with open('eggs.csv', newline='') as csvfile:
# ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# ...     for row in spamreader:
# ...         print(', '.join(row))
# Spam, Spam, Spam, Spam, Spam, Baked Beans
# Spam, Lovely Spam, Wonderful Spam
#
# import nltk
# import pandas as pd
# from nltk.corpus import stopwords
# #nltk.download('stopwords')
# from nltk.corpus import gutenberg
# from nltk.text import Text
# from nltk.probability import FreqDist
# import regex as re
# import matplotlib.pyplot as plt
# import numpy as np

import csv
import operator

list1 = list()
with open('ca-500_avec_dups.csv', 'rt', encoding='UTF8') as f_csv:
    csv_reader = csv.DictReader(f_csv)
    for row in csv_reader:
        list1.append(row)


# list2 = sorted(csv1, key=operator.itemgetter(1, 2))
sorted_list2 = sorted(list1, key=lambda x: x['phone1'])
for i in sorted_list2:
    print(i['phone1'] + " " + i['last_name'] )

print('########################################################################################################')
sorted_list3 = sorted(sorted_list2, key=lambda x: x['last_name'])
for k in sorted_list3:
    print(k['phone1'] + " " + k['last_name'] )



