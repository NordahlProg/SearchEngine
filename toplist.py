import numpy as np

def topList(array,filelist):
    ind = np.argpartition(array,-10)[-10:]
    sortedmax = ind[np.argsort(array[ind])][::-1]
    for i in sortedmax:
        print(filelist[i])