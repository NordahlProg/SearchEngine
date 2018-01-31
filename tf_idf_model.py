import math
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import cleaning_module as cl
from sklearn.metrics.pairwise import cosine_similarity



def tfidf(query,filelist):
    query = cl.regex_clean(query)
    l = cl.bodyTextTransform(filelist, query)
    t = CountVectorizer().fit_transform(l)
    tfidf = TfidfTransformer().fit_transform(t)
    similarities = cosine_similarity(tfidf, dense_output=False)
    y = similarities[len(filelist), 0:len(filelist)]
    y = y.toarray()[0]
    return y
