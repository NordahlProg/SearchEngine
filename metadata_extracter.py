import re

def companyNameExtract(filelist):
    l = list()
    for d in filelist:
        vec = re.split("_[0-9][0-9][0-9][0-9]",d)[0]
        vec = re.sub(".pdf|['&\(\)]","",vec)
        vec = re.sub("_{1,}|-"," ",vec)
        vec = re.sub("[0-9]","",vec)
        l.append(vec)
    return(l)
