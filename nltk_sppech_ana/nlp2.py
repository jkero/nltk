import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer
import regex as re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
#from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop

#nltk.download('omw-1.4')

text = "Natural language processing is an exciting area."

print(sent_tokenize(text))

print(word_tokenize(text))

text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
words = text.split()
print(words)
print(stopwords.words("english"))
print(stopwords.words("french"))
print(stopwords.words("italian"))

# Reduce words to their stems
stemmed = [PorterStemmer().stem(w) for w in words]
print(stemmed)

lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]
print(lemmed)

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]

grammar = "NP: {<DT>?<JJ>*<NN>}"

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print(result)
result.draw()