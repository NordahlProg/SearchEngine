import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import textract


def regex_clean(text):
    newtext = re.sub(r"\\x..", "", text)
    newtext = re.sub(r"\\n[0-9]", "", newtext)
    newtext = re.sub(r"\\n", "", newtext)
    newtext = re.sub(r"(\\r)+", " ", newtext)
    newtext = re.sub("b'", "", newtext)
    newtext = re.sub("\"|b\"", "", newtext)
    newtext = re.sub(" {2,}|-", " ", newtext)
    newtext = re.sub("['?!+&_.,;%><*=@¤#£¨^$~:\[\]\{\}\|\/\(\)]|[0-9]","", newtext)
    newtext = newtext.lower()
    return newtext

def regex_titleclean(title):
    newtitle = re.sub(" {2,}|[_-]"," ",title)
    newtitle = re.sub("[&'\(\)]|.pdf","",newtitle)
    return newtitle

def titleTransform(titlelist):
    for m, d in enumerate(titlelist):
        newtitle = regex_titleclean(d)
        strvec = re.split(" ", newtitle)
        for i, j in enumerate(strvec):
            stringlist = re.findall("[A-Z][a-z]", j[2:])
            for k in stringlist:
                if len(k) > 1:
                    j = re.sub(k, " " + k, j)
            if re.match("2[0-9]",j):
                j = j[0:4]
            strvec[i] = j
        s = ''
        for ff in strvec:
            s = s + " " + ff
        s = s.lower()
        titlelist[m] = re.sub(" {2,}"," ",s)
    return titlelist

def bodyTextTransform(titlelist):
    l = list()
    stops = set(stopwords.words('english'))
    ps = PorterStemmer()
    for d in titlelist:
        text = regex_clean(str(textract.process(d)))
        words = word_tokenize(text)
        filtered = [w for w in words if not w in stops]
        stemmedWords = [ps.stem(w) for w in filtered]
        l.append(stemmedWords)
    return l
