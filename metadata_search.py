import re

def tf(query,filelist):
    qvec = query.split(" ")
    l = list()
    for d in filelist:
        dvec = d.split(" ")
        l.append(len(set(qvec)&set(dvec)))
    return l

def containsYear(query):
    return re.search("20[0-9][0-9]",query)


