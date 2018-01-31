import re
import numpy as np
import cleaning_module as cl
from query_transformer import queryTransform
import spacy
nlp = spacy.load('en_core_web_lg')


def metaScore(query,filelist,a,b,c):
    filelist = cl.titleTransform(filelist)
    query = queryTransform(query)
    doc1 = nlp(query)
    l = list()
    l2 = list()
    l3 = list()
    qvec = query.split(" ")
    match = re.search("20[0-9][0-9]", query)
    if(match):
        year = match.group(0)
        for d in filelist:
            if year in d:
                l2.append(1)
            else:
                l2.append(0)
    else:
        l2 = [0]*len(filelist)

    for d in filelist:
        d = re.sub("[0-9]","",d)
        doc2 = nlp(d)
        dist = doc1.similarity(doc2)
        l3.append(dist)
        dvec = d.split(" ")
        l.append(len(set(qvec)&set(dvec)))
    return a*np.asarray(l) + b*np.asarray(l2) + c*np.asarray(l3)