from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re

def queryClean(q):
    q = q.lower()
    q = re.sub(" {2,}|-", " ", q)
    q = re.sub("['?!+&_.,;%><*=@¤#£¨^$~:\[\]\{\}\|\/\(\)]","", q)
    return q

def queryTransform(q):
    q = queryClean(q)
    ps = PorterStemmer()
    words = word_tokenize(q)
    stops = set(stopwords.words('english'))
    filtered = [w for w in words if not w in stops]
    q = [ps.stem(w) for w in filtered]
    q = ' '.join(q)
    return q