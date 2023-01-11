import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.probability import FreqDist
import regex as re
import matplotlib.pyplot as plt

f_stop =  stopwords.words('french')

autre_stops =[",","'","--",".",";","a","cette","cet","plus","comme","tout","toute",'’',":","où","?",'!',"«","»",'toutes','après','(',")"]
for i in autre_stops:
    f_stop.append(i)
with open('boivert_boutin_2022.txt', 'rt', encoding='UTF8') as f:
     bb = f.read()
c_text = str(bb.lower())
t_text = nltk.word_tokenize(c_text)
# text.dispersion_plot(['sourire','horreur','félicité'])
f_text = nltk.Text(t_text)

t_sans_sw = [word for word in f_text if not word in f_stop]

fdist = FreqDist(t_sans_sw).most_common(15)

cfdist = nltk.ConditionalFreqDist()

for ix in range (0, len(fdist)):
     condition = fdist[ix][0] != 0
     cfdist[condition][fdist[ix][1]] += 1

# for condition in cfdist:
#     print(condition)

# for condition in cfdist:
#     for word in cfdist[condition]:
#         print("Cond. frequency of " + str(word) + " " +  str(cfdist[condition].freq(word)) +  " [condition is word length =" + "  " + str(condition) + "]")


def add_value_label(x_list,y_list):
    for i in range(1, len(x_list)+1):
        plt.text(i,y_list[i-1],y_list[i-1], ha="center")

def add_value_label2(x_list,y_list):
    for i in range(1, len(x_list)+1):
        plt.text(i,y_list[i-1]/2,y_list[i-1], ha="left")

print(str(fdist))

#Exercice ConditionalFreqDist ??

#cvs = [cv for w in fdist for cv in re.findall(r'[kim][boutin]', w)](?=.*word1)(?=.*word2)(?=.*word3)
# cvs = [('kim', word) for word in t_sans_sw]
cfdist.tabulate()

# cfd = nltk.ConditionalFreqDist(cvs)
# cfd.tabulate()
for i in range(0,len(fdist)):
    plt.text(i, fdist[i][1]+ .1, fdist[i][1])

plt.bar(range(len(fdist)), [val[1] for val in fdist], align='center')
plt.xticks(range(len(fdist)), [val[0] for val in fdist])
plt.xticks(rotation=70)
plt.show()
#
# cvs =
# cfd = nltk.ConditionalFreqDist(cvs)
# cfd.tabulate()

# cfd = [('gas', word) for word in brown.words(categories='gas')]
# cfd.tabulate(conditions=['gas'], samples=['gasoline', 'barrels']
#
# ----------------
# Output:
#     gasoline  barrels
# gas       77       64
#
# for word in word_tokenize(text):
#     condition = len(word)
#     cfdist[condition][word] += 1
#
# for condition in cfdist:
#     for word in cfdist[condition]:
#         print "Cond. frequency of", word, cfdist[condition].freq(word), "[condition is word length =", condition, "]"

