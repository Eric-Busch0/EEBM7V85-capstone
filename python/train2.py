import requests
import scipy.io
import numpy as np
import json
from json import JSONEncoder
import matplotlib.pyplot as plt
import pandas as pd
from ecgdetectors import Detectors
import pickle
from tkinter import Y
import scipy.io
from sklearn import svm
from itertools import chain
import numpy as np
import pickle

fs = 360
ts = 1 / 360
detectors = Detectors(fs)
ENDPOINT = "http://127.0.0.1:5000"

y_test = scipy.io.loadmat('ytest.mat')['y_test']
y_train = scipy.io.loadmat('ytrain.mat')['y_train']



ecg = scipy.io.loadmat('100m.mat')['val']

a = 0
b = 255
length = len(ecg[0])
lower = min(ecg[0])
upper = max(ecg[0])

for i in range(length):
    ecg[0][i] = (b - a) * (ecg[0][i] -lower) / (upper - lower) + a
with open('ecg.npy', 'wb') as f:
    np.save(f, ecg)    

# print(ecg[0])
# print(max(ecg[0]))
r_peaks = detectors.pan_tompkins_detector(ecg[0])
# plt.plot(ecg[0][0:256])
# plt.show()
# plt.plot(ecg[0][r_peaks[0] - 50 : r_peaks[0] + 50])
# plt.show()
first_half = r_peaks[2:]
first_half = np.multiply(np.array(ts), first_half)
second_half = r_peaks[1 : -1]
second_half = np.multiply(np.array(ts), second_half)

pre_rr = np.subtract(first_half, second_half)
post_rr = pre_rr[2:-1]

post_rr = np.append(post_rr, [pre_rr[-2], pre_rr[-1] ])
modelData = []
for i in range(len(post_rr)):
    modelData.append([int(pre_rr[i] * 100), int(post_rr[i] * 100)])

    
        
print(len(modelData))
x_train = modelData[0:1798]
x_test = modelData[1798:]
print(len(x_test))
clf = svm.SVC()
clf.fit(x_train, y_train.ravel())

ret = clf.score(x_test,y_test[:471])

print("Accuracy: "  + str(ret * 100) + "%")

filename = 'ecg_svm2'
pickle.dump(clf, open(filename, 'wb'))

