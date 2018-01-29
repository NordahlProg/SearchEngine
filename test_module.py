import nltk
import re
import textract
import os
import spacy
import numpy as np
import cleaning_module as cl
from metadata_search import tf
import ppt_to_pdf_module
import query_transformer
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
from nltk.tokenize import PunktSentenceTokenizer
nltk.download("wordnet")


ps = PorterStemmer()
nlp = spacy.load('en_core_web_sm')
nlp2 = spacy.load('en_vectors_web_lg')
dir = "C:/Users/tnordahl/Desktop/GDSCDataSet/Presentations/train_data"
os.chdir(dir)
filelist = os.listdir()
filelist2 = os.listdir()
query = "2013"
query = query_transformer.queryClean(query)

print(re.search("20[0-9][0-9]",query))
#vec = cl.titleTransform(filelist)

#l = tf(query,vec)

#for i in l:
#    print(i)

