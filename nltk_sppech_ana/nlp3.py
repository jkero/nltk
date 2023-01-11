import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.probability import FreqDist

import matplotlib.pyplot as plt

#print(type(text6))

f_stop =  stopwords.words('french')

autre_stops =[",","'","--",".",";","a","cette","cet","plus","comme","tout","toute",'’',":","où","?",'!',"«","»",'toutes','après']
for i in autre_stops:
    f_stop.append(i)

print (f_stop)

with open('corpus_francais\\homme_qui_rit.txt', 'rt' ,encoding='UTF8') as f:
     hugo = f.read()
c_text = str(hugo.lower())
t_text = nltk.word_tokenize(c_text)
# text.dispersion_plot(['sourire','horreur','félicité'])
f_text = nltk.Text(t_text)



texte_sans_sw = [word for word in f_text if not word in f_stop]


fdist=FreqDist(texte_sans_sw)

mc100 = list(fdist.most_common(100))

plt.bar(range(len(mc100)), [val[1] for val in mc100], align='center')
plt.xticks(range(len(mc100)), [val[0] for val in mc100])
plt.xticks(rotation=70)
plt.show()


# print(len(f_text))
# print(f_text.collocations(33))
#
# print(f_text.concordance("monstrueux"))

# cfd = nltk.ConditionalFreqDist((word) for word in text)
#
# modals =['amour','horeur']
#
# cfd.tabulate(samples = modals)

#[(',', 18033), ('’', 13745), ('.', 13475), ('--', 1815), ('Il', 1579), (';', 1357), ('!', 1191), ('?', 1007), ('a', 986), ('Le', 898), ('plus', 897), ('Gwynplaine', 860), ('cette', 798), ('comme', 754), (':', 740), ('La', 672), ('tout', 618), ('L', 599), ('C', 597), ('deux', 526), ('Ursus', 505), ('On', 493), ('Les', 477), ('fait', 474), ('où', 472), ('être', 417), ('homme', 413), ('Je', 390), ('dit', 387), ('Ce', 354), ('autre', 346), ('Dea', 335), ('Et', 324), ('Elle', 321), ('«', 319), ('sous', 314), ('cela', 314), ('lord', 304), ('là', 295), ('point', 293), ('sans', 289), ('bien', 282), ('peu', 268), ('Un', 267), ('si', 250), ('Angleterre', 249), ('roi', 241), ('enfant', 238), ('A', 231), ('femme', 220), ('faisait', 216), ('»', 209), ('faire', 207), ('rien', 206), ('entre', 204), ('tous', 203), ('mer', 202), ('Cette', 200), ('Une', 198), ('Ils', 191), ('temps', 191), ('chose', 189), ('tête', 187), ('cet', 186), ('En', 184), ('devant', 183), ('nuit', 182), ('porte', 178), ('dont', 175), ('toutes', 172), ('lords', 170), ('the', 168), ('toute', 167), ('côté', 163), ('très', 159), ('Mais', 159), ('Tout', 158), ('J', 157), ('Barkilphedro', 157), ('quelque', 156), ('encore', 154), ('avoir', 153), ('chambre', 152), ('Vous', 152), ('voix', 150), ('vie', 149), ('jour', 147), ('hommes', 147), ('De', 144), ('terre', 144), ('peut', 141), ('puis', 141), ('près', 136), ('Josiane', 136), ('aussi', 135), ('fit', 134), ('coup', 134), ('trois', 131), ('Qu', 131), ('Dans', 129)]
