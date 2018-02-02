import os
import spacy
import ppt_to_pdf_module
from metadata_search import metaScore
from toplist import topList
from tf_idf_model import tfidf
import cleaning_module as cl
from query_transformer import queryTransform
nlp = spacy.load('en_core_web_lg')
import numpy as np

a=1 #hyperparameter for text matching in metadata
b=1 #hyperparameter for year matching in metadata
c=0.5 #hyperparameter for word vector similarity in metadata

dir = "C:/Users/tnordahl/Desktop/GDSCDataSet/Presentations/train_data"
os.chdir(dir)
filelist = os.listdir()
filelist2 = os.listdir()
query = "big data project"

doc1 = nlp(query)
l2 = list()
texts = cl.bodyTextTransform(filelist,query,stemming=False)
for t in texts:
    doc2 = nlp(t)
    l2.append(doc1.similarity(doc2))

for k in l2:
    print(k)

#vec1 = metaScore(query,filelist,a,b,c)
#vec2 = tfidf(query,filelist2)
#vec3 = vec1+vec2
#topList(vec3,filelist2)

