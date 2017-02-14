import numpy as np
import matplotlib.pyplot as pp
from sklearn import svm, preprocessing
from sklearn.model_selection import cross_val_score
import h5py

data = []
with open('./data/solubility_encoded.txt') as f:
    for line in f:
        temp = line.rstrip('\n')
        temp = temp.split('\t')
        temp = [float(x) for x in temp]
        data.append(temp)
    f.close()
X_train = np.array(data)
X_train = preprocessing.scale(X_train)
h5f = h5py.File('./data/processed_solubility.h5', 'r')
data = h5f['.']['solubility'].value
data = [ float(x) for x in data]
y_train = np.array(data)
clf = svm.SVR(kernel='rbf')
print np.mean(cross_val_score(clf, X_train, y_train,cv=5,scoring='r2'))
