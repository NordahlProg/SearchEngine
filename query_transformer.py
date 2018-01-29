import cleaning_module as cl
import spacy

def queryClean(q):
    q = q.lower()
    q = cl.regex_clean(q)
    return q

