import nltk
import textract
import os
import io
import spacy
import numpy as np
import cleaning_module as cl
import ppt_to_pdf_module

nlp = spacy.load('en_core_web_lg')
dir = "C:/Users/tnordahl/Desktop/GDSCDataSet/Presentations/train_data"
os.chdir(dir)
filelist = os.listdir()
filelist2 = os.listdir()
query = "IoT"

filelist = cl.titleTransform(filelist)

vec = [nlp(d).similarity(nlp(query)) for d in filelist]

array = np.asarray(vec)
ind = np.argpartition(array,-10)[-10:]
sortedmax = ind[np.argsort(array[ind])][::-1]
for i in sortedmax:
    print(filelist2[i])