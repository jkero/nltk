import nltk
import re
from nltk.corpus import stopwords


from nltk.corpus import stopwords

with open('stop_words_french.txt',encoding="utf-8") as f:
    stop_word_lines = f.read().splitlines()

with open('embau.txt',encoding="utf-8") as f2:
    manuel_employe = f2.read()
words = manuel_employe.split()
print("1 le fichier texte brut donne " + str(len(words)) + " mots")
words_sans_empty = [x2.strip("\;:,'!%?/") for x2 in words if x2 != '']
setwords = set(words_sans_empty)
print("1a le fichier texte sans doublons donne " + str(len(setwords)) + " mots")


words2 = re.split('[\\n,;:\\s]',manuel_employe) #j'essaie d'utiliser les séparateurs newline, ponctuations et espace
print("2 le fichier RE texte brut donne " + str(len(words2)) + " mots")
words2_sans_empty = [x2 for x2 in words2 if x2 != '']
setwords2 = set(words2_sans_empty)
print("2a le fichier RE texte sans doublons donne " + str(len(setwords2)) + " mots")




stop_words = set(stopwords.words('french'))

#add words that aren't in the NLTK stopwords list
new_stopwords = stop_word_lines
new_stopwords_list = stop_words.union(new_stopwords)

#remove words that are in NLTK stopwords list
not_stopwords = {'momo'}
final_stop_words = set([word for word in new_stopwords_list if word not in not_stopwords])

#print(final_stop_words + "  " + str(final_stop_words)
# print("\n stopwords")
# print (final_stop_words)
# print("__________"+  str(len(final_stop_words)) +  "_______________")
# print("\n basic split function")
# print (words_sans_empty)
# print("__________" +  str(len(words_sans_empty)) + "_______________")
# print("\n re.split function")
# print (words2_sans_empty)
# print("___________" +  str(len(words2_sans_empty)) + "_______________")
print("\n basic split is now a set")
print (setwords)
print("__________" +  str(len(setwords)) + "________________")
print("\n  re.split is now a set")
print (setwords2)
print("____________" +  str(len(setwords2)) + "______________")

print("\n Enlever stop words de basic split set")
sans_sw = [x for x in setwords if x not in final_stop_words]
print("____________" +  str(len(sans_sw)) + "______________")

print("Enlever stop words de re.split set")
sans_sw2 = [x2 for x2 in setwords2 if x2 not in final_stop_words]
print("____________" +  str(len(sans_sw2)) + "______________")

print("\n test diff 2 sets basic - re : les ponctuations font une différence")
dif = setwords.difference(setwords2)
print (len(dif))
print(dif)
