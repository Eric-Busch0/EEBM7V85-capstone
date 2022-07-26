from tkinter import Y
import scipy.io
from sklearn import svm
from itertools import chain
import numpy as np
import pickle

#probably gonna lose some accuracy because of the int and not fload but float is too much of a pain to send of a pain to send over serial
# 0 - 100 only requires 1 bytes instead of 4 bytes for a float
x_test = scipy.io.loadmat('xtest.mat')['x_test'].astype(int)
y_test = scipy.io.loadmat('ytest.mat')['y_test']
x_train = scipy.io.loadmat('xtrain.mat')['x_train'].astype(int)
y_train = scipy.io.loadmat('ytrain.mat')['y_train']

x_test = np.multiply(x_test, [100]).astype(int)

print(x_train)



clf = svm.SVC()
clf.fit(x_train, y_train.ravel())

ret = clf.score(x_test,y_test)

print("Accuracy: "  + str(ret * 100) + "%")

filename = 'ecg_svm'
pickle.dump(clf, open(filename, 'wb'))

