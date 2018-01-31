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

a=1
b=1
c=0.5

dir = "C:/Users/tnordahl/Desktop/GDSCDataSet/Presentations/train_data"
os.chdir(dir)
filelist = os.listdir()
filelist2 = os.listdir()
query = "hospital"

vec1 = metaScore(query,filelist,a,b,c)
vec2 = tfidf(query,filelist2)
vec3 = vec1+vec2
topList(vec3,filelist2)


#topList(np.asarray(l),filelist2)