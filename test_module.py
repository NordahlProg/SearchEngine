import os
import spacy
import ppt_to_pdf_module
from metadata_search import metaScore
from toplist import topList
from tf_idf_model import tfidf


a=1
b=1
dir = "C:/Users/tnordahl/Desktop/GDSCDataSet/Presentations/train_data"
os.chdir(dir)
filelist = os.listdir()
filelist2 = os.listdir()
query = "entercard"

vec1 = metaScore(query,filelist,a,b)
vec2 = tfidf(query,filelist2)
vec3 = vec1+vec2

topList(vec3,filelist2)