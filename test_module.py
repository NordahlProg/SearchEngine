import os
import spacy
import ppt_to_pdf_module
from metadata_search import metaScore
from toplist import topList
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import cleaning_module as cl
from sklearn.metrics.pairwise import cosine_similarity
from tf_idf_model import tfidf



a=1
b=1
dir = "C:/Users/tnordahl/Desktop/GDSCDataSet/Presentations/train_data"
os.chdir(dir)
filelist = os.listdir()
filelist2 = os.listdir()
query = "watson 2016"

vec1 = metaScore(query,filelist,a,b)
vec2 = tfidf(query,filelist2)
vec3 = vec1+vec2

print(topList(vec3,filelist2))