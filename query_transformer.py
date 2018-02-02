from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re

def queryClean(q):
    q = q.lower()
    q = re.sub(" {2,}|-", " ", q)
    q = re.sub("['?!+&_.,;%><*=@¤#£¨^$~:\[\]\{\}\|\/\(\)]","", q)
    return q

def queryTransform(q,stemming):
    q = queryClean(q)
    words = word_tokenize(q)
    stops = set(stopwords.words('english'))
    q = [w for w in words if not w in q]
    if stemming:
        ps = PorterStemmer()
        q = [ps.stem(w) for w in q]
    q = ' '.join(q)
    return q