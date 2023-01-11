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

autre_stops =[",","'","--",".",";","a","cette","cet","plus","comme","tout","toute",'’',":","où","?",'!',"«","»",'toutes','après','(',")"]
for i in autre_stops:
    f_stop.append(i)

with open('corpus_francais\homme_qui_rit.txt ', 'rt', encoding='UTF8') as f:
    bb = f.read()
c_text = str(bb.lower())
t_text = nltk.word_tokenize(c_text)

set_texte =   sorted(set(t_text))

fd = nltk.FreqDist([(vs) for mot in set_texte for vs in re.findall(r'\b([a-z]*able)|(\b[a-z]*ique)', mot)])
# print(fd.items())

#fd = [(('', 'abdique'), 1), (('abominable', ''), 2), (('abordable', ''), 2), (('accable', ''), 3), (('', 'acoustique'), 1), (('admirable', ''), 3), (('adorable', ''), 2), (('affable', ''), 1), (('aimable', ''), 2), (('', 'antique'), 2), (('', 'apoplectique'), 1), (('applicable', ''), 1), (('', 'applique'), 3), (('', 'aquatique'), 1), (('', 'aristocratique'), 1), (('arrachable', ''), 1), (('', 'atlantique'), 1), (('', 'aulique'), 1), (('', 'authentique'), 2), (('', 'automatique'), 2), (('available', ''), 1), (('', 'barrique'), 1), (('', 'belgique'), 1), (('', 'bellique'), 1), (('', 'biblique'), 1), (('', 'bourrique'), 1), (('', 'boutique'), 2), (('', 'brique'), 2), (('', 'britannique'), 1), (('', 'bucolique'), 2), (('cable', ''), 1), (('capable', ''), 2), (('', 'casuistique'), 1), (('', 'catholique'), 2), (('charitable', ''), 1), (('', 'chique'), 1), (('', 'chronique'), 1), (('', 'chronologique'), 1), (('', 'classique'), 1), (('', 'clinique'), 1), (('', 'clique'), 1), (('', 'comique'), 1), (('', 'communique'), 1), (('comparable', ''), 1), (('', 'complique'), 3), (('confortable', ''), 1), (('considerable', ''), 1), (('constable', ''), 1), (('contribuable', ''), 1), (('convenable', ''), 2), (('', 'cosmique'), 1), (('coupable', ''), 1), (('', 'crique'), 2), (('', 'critique'), 2), (('', 'cynique'), 2), (('', 'dalmatique'), 1), (('damnable', ''), 1), (('', 'despotique'), 1), (('diable', ''), 3), (('', 'diabolique'), 3), (('', 'dioptrique'), 1), (('', 'diplomatique'), 1), (('', 'docminique'), 1), (('', 'domestique'), 2), (('dunstable', ''), 1), (('effroyable', ''), 1), (('entable', ''), 2), (('', 'explique'), 4), (('', 'extatique'), 2), (('fable', ''), 1), (('', 'fabrique'), 3), (('faisable', ''), 2), (('', 'fantasmagorique'), 1), (('', 'fantastique'), 1), (('favorable', ''), 2), (('', 'flegmatique'), 1), (('formidable', ''), 3), (('friable', ''), 1), (('', 'germanique'), 1), (('', 'gothique'), 2), (('', 'gymnastique'), 1), (('habitable', ''), 2), (('', 'hippocratique'), 1), (('', 'historique'), 1), (('honorable', ''), 2), (('honourable', ''), 2), (('', 'horrifique'), 1), (('', 'hydraulique'), 1), (('', 'identique'), 1), (('immuable', ''), 1), (('impalpable', ''), 1), (('imperdable', ''), 1), (('imperturbable', ''), 2), (('impitoyable', ''), 1), (('implacable', ''), 1), (('', 'implique'), 1), (('impraticable', ''), 1), (('imprenable', ''), 1), (('', 'impudique'), 1), (('inabordable', ''), 1), (('inarrachable', ''), 1), (('inavouable', ''), 2), (('incapable', ''), 2), (('incommensurable', ''), 3), (('incomparable', ''), 1), (('inconsolable', ''), 1), (('incontestable', ''), 3), (('incroyable', ''), 1), (('incurable', ''), 2), (('', 'indique'), 3), (('indispensable', ''), 2), (('indomptable', ''), 1), (('ineffable', ''), 1), (('inestimable', ''), 1), (('inexorable', ''), 3), (('inexprimable', ''), 2), (('inexpugnable', ''), 1), (('inextricable', ''), 1), (('infranchissable', ''), 1), (('inimaginable', ''), 1), (('innombrable', ''), 1), (('insaisissable', ''), 1), (('insondable', ''), 1), (('insupportable', ''), 2), (('insurmontable', ''), 1), (('intraitable', ''), 1), (('invariable', ''), 1), (('inviolable', ''), 1), (('invraisemblable', ''), 2), (('', 'ironique'), 1), (('irresponsable', ''), 1), (('irritable', ''), 1), (('', 'juridique'), 1), (('justiciable', ''), 2), (('justifiable', ''), 1), (('lamentable', ''), 3), (('liable', ''), 1), (('logeable', ''), 1), (('', 'logique'), 2), (('louable', ''), 2), (('', 'lubrique'), 1), (('', 'lyrique'), 1), (('', 'magique'), 1), (('', 'magnifique'), 3), (('maniable', ''), 1), (('', 'mexique'), 1), (('', 'microscopique'), 2), (('', 'monarchique'), 2), (('', 'morganatique'), 1), (('', 'mozarabique'), 1), (('', 'musique'), 3), (('', 'mythologique'), 1), (('', 'nitrique'), 1), (('', 'oblique'), 2), (('', 'olympique'), 1), (('', 'optique'), 1), (('', 'pacifique'), 2), (('palpable', ''), 1), (('', 'panique'), 1), (('', 'paralytique'), 1), (('passable', ''), 1), (('', 'pathologique'), 1), (('', 'patriotique'), 2), (('', 'philosophique'), 1), (('', 'physique'), 1), (('', 'pique'), 4), (('pitoyable', ''), 1), (('', 'plastique'), 1), (('', 'politique'), 1), (('praticable', ''), 2), (('', 'pratique'), 4), (('probable', ''), 3), (('profitable', ''), 1), (('', 'publique'), 3), (('', 'pudique'), 1), (('', 'punique'), 1), (('punissable', ''), 1), (('', 'quoique'), 1), (('', 'rabique'), 1), (('raisonnable', ''), 1), (('readable', ''), 1), (('reasonable', ''), 1), (('reconnaissable', ''), 2), (('redevable', ''), 1), (('redoutable', ''), 2), (('refusable', ''), 1), (('', 'relique'), 1), (('remarquable', ''), 2), (('reprochable', ''), 1), (('respectable', ''), 2), (('respirable', ''), 1), (('responsable', ''), 2), (('', 'rhythmique'), 1), (('', 'rustique'), 1), (('sable', ''), 2), (('saisissable', ''), 1), (('', 'salique'), 1), (('', 'satanique'), 1), (('', 'schismatique'), 1), (('', 'scientifique'), 2), (('secourable', ''), 1), (('semblable', ''), 2), (('', 'sobrique'), 1), (('souhaitable', ''), 1), (('', 'statique'), 1), (('', 'supplique'), 1), (('table', ''), 4), (('', 'tactique'), 1), (('', 'titanique'), 1), (('', 'tonique'), 1), (('', 'tournique'), 1), (('', 'tragique'), 3), (('', 'transatlantique'), 1), (('trouvable', ''), 1), (('', 'tyrannique'), 1), (('', 'unique'), 2), (('', 'viatique'), 1), (('vraisemblable', ''), 2), (('', 'zygomatique'), 1)]
data_terme = []
data_occu = []
for i in fd.items():
    for j in i[0]:
        if j != '':
            data_terme.append(j)
            data_occu.append(i[1])
print(data_terme)
print(data_occu)

data = {'occurrences':data_occu,
        'termes':data_terme
        }

df = pd.DataFrame(data, columns=['occurrences'], index=data['termes'])
df.sort_values(by=['occurrences'], inplace=True)
df.plot.barh()
plt.show()