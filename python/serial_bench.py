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

import serial

data = np.load('ecg.npy')[0].astype(np.uint8)
print("running")
ser = serial.Serial('COM6',timeout=1)
ser.write(data)
ser.close()