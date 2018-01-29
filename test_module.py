import nltk
import textract
import os
import spacy
import ppt_to_pdf_module
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
from nltk.tokenize import PunktSentenceTokenizer
from metadata_search import metaScore
import toplist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import cleaning_module as cl
nltk.download('stopwords')

a=1
b=3

dir = "C:/Users/tnordahl/Desktop/GDSCDataSet/Presentations/train_data"
os.chdir(dir)
filelist = os.listdir()
filelist2 = os.listdir()
query = "audi 2012"
stops = set(stopwords.words('english'))
d = filelist[8]
text = cl.regex_clean(str(textract.process(d)))
words = word_tokenize(text)
filtered = [w for w in words if not w in stops]
for f in filtered:
    print(f)

#meta_scores = metaScore(query,filelist2,a,b)
#toplist.topList(meta_scores,filelist)