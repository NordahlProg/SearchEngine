import re
import numpy as np
import cleaning_module as cl
from query_transformer import queryClean

def metaScore(query,filelist,a,b):
    filelist = cl.titleTransform(filelist)
    query = queryClean(query)
    l = list()
    l2 = list()
    qvec = query.split(" ")
    match = re.search("20[0-9][0-9]", query)
    for d in filelist:
        dvec = d.split(" ")
        l.append(len(set(qvec)&set(dvec)))

    if(match):
        year = match.group(0)
        for d in filelist:
            if year in d:
                l2.append(1)
            else:
                l2.append(0)
    else:
        l2 = [0]*len(filelist)
    return a*np.asarray(l) + b*np.asarray(l2)