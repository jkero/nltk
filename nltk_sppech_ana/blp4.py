import nltk
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.probability import FreqDist

c_text = "ma mère chantait toujours, la la la, une belle chanson d'amour que je te chante à mon tour"
t_text = nltk.word_tokenize(c_text)
# text.dispersion_plot(['sourire','horreur','félicité'])
f_text = nltk.Text(t_text)

fdist=FreqDist(f_text)
print (fdist.most_common(3))