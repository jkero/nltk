import nltk
import pandas as pd
from nltk.corpus import stopwords
#nltk.download('stopwords')
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.probability import FreqDist
import regex as re
import matplotlib.pyplot as plt
import numpy as np

pd.options.plotting.backend = 'matplotlib'

f_stop =  stopwords.words('french')

autre_stops =["fait","sous","m.","j'ai","of","quand","quelque","fit","aussi","ainsi","là","puis","c'est","sans","cela","qu'on","qu'elle","the","n'est","faire",'si',"qu'il","c'était","d'un","d'une",",","'","--",".",";","a","cette",'',"cet","plus","comme","tout","toute",'’',":","où","?",'!',"«","»",'toutes','après','(',")", ']','[']
for i in autre_stops:
    f_stop.append(i)

with open('.\\corpus_varie\\avare.txt', 'rt', encoding='UTF8') as f:
    bb = f.read()
c_text = str(bb.lower())
t_text = nltk.word_tokenize(c_text)

#débarasse/filtre les stopwords
texte_sans_sw = [word for word in t_text if not word in f_stop]

# option 1 fd = nltk.FreqDist(texte_sans_sw)
fd_all = nltk.FreqDist(texte_sans_sw)

#option 2 avec critères de comparaison et sélection
fd_regex = nltk.FreqDist([(vs) for mot in texte_sans_sw for vs in re.findall(r'\b([a-zéâàêèîëôöüùû]*voil[a-za-zéàêôèîëùöü]*)|(\b[a-za-zéàêôèîëùöü]*iande[a-za-zéàêôèîëùöü]*)', mot)])

#option3: recherche d'expressions qui terminent par ube particule (comme une conjugaison à l'imparfait -*ait)
hyb = [x for x in re.finditer('((\\b[a-zéâàêèîëôöüùû’]*\\b ){2,4})(?=([a-zéâàêèîëôöüùû’]*ait))',c_text)]
grps = []
for i in hyb:
    grps.append((str(i[0]) + str(i[3])).replace(' ','~'))

fd_grp = nltk.FreqDist(grps)

print("fd_all =" + str(fd_all))
mc100 = list(fd_all.most_common(100))
print(mc100)
print("-------------------------------------------------------------------------------------------------")
print("fd_regex =" + str(fd_regex))
mc101 = list(fd_regex.most_common(100))
print(mc101)
print("-------------------------------------------------------------------------------------------------")
print("fd_grps =" + str(fd_grp))
mc102 = list(fd_grp.most_common(100))
print(mc102)

data_terme = []
data_occu = []
va_terme = ""
for i in mc101:
    if type(i[0]) is tuple:
        for j in i[0]:
            if len(j) > 0:
                va_terme = j
                data_terme.append(va_terme)
                data_occu.append(i[1])
                break
    else:
        va_terme = i[0]
        if i[1] > 1:
            if i[0] != '':
                data_terme.append(va_terme)
                data_occu.append(i[1])

print("------------ TERME--------------")
print(data_terme)
print("------------ OCCU--------------")
print(data_occu)
print("------------ MAX--------------")
print(max(data_occu))

# je suppose que composer des séries était plus utile et souple
data = {'occurrences':data_occu,
        'termes':data_terme
        }
#
df = pd.DataFrame(data, columns=['occurrences'], index=data['termes'])
df.sort_values(by=['occurrences'], inplace=True)
plt.rcParams["figure.figsize"] = (15,9)
interv = int(max(data_occu)/50) if max(data_occu) > 100 else int(max(data_occu)/4)
xticks = np.arange(0, max(data_occu), interv)
fig, ax = plt.subplots()
ax.barh(data_terme, data_occu)
ax.invert_yaxis()
ax.set_ylabel('Termes')
ax.set_xlabel('Occurrences')
ax.xaxis.grid(True, color ="grey")

ax.set_xticks(xticks)
#df.plot.barh().grid(True, color = "green", linewidth = ".5", linestyle = "dotted")
plt.show()