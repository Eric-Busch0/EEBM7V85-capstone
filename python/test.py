
import requests
import scipy.io
import numpy as np
import json
from json import JSONEncoder
import matplotlib.pyplot as plt
import pandas as pd
from ecgdetectors import Detectors
import pickle

fs = 360
ts = 1 / 360
detectors = Detectors(fs)
ENDPOINT = "http://127.0.0.1:5000"



ecg = scipy.io.loadmat('100m.mat')['val']

a = 0
b = 255
print(len(ecg[0]))
length = len(ecg[0])
lower = min(ecg[0])
upper = max(ecg[0])

for i in range(length):
    ecg[0][i] = (b - a) * (ecg[0][i] -lower) / (upper - lower) + a
    

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
print(post_rr)

post_rr = np.append(post_rr, [pre_rr[-2], pre_rr[-1] ])
modelData = []
for i in range(len(post_rr)):
    modelData.append([int(pre_rr[i] * 100), int(post_rr[i] * 100)])
    

# print(modelData)
# filename = 'ecg_svm'
# model = pickle.load(open(filename, 'rb'))
# modelData = np.array(modelData)
# ans = model.predict(modelData)
# print(modelData)
# x_test = scipy.io.loadmat('xtest.mat')['x_test'].astype(int)

    
# ans = model.predict(modelData)
# print(ans)

# x_test = scipy.io.loadmat('xtest.mat')['x_test'].astype(int)
# data0 = np.transpose(x_test)[0].tolist()
# data1 = np.transpose(x_test)[1].tolist()
# json_str = json.dumps({'data' :ecg.tolist()})
# resp = requests.post(ENDPOINT, json=json_str)
# if resp.status_code == 200:
#     print(resp.content)
# else:
#     print(resp.status_code)