
import numpy as np

from json import JSONEncoder
import matplotlib.pyplot as plt
import pandas as pd

from tkinter import Y
import scipy.io
from sklearn import svm
from itertools import chain
import numpy as np


import serial

data = np.load('ecg.npy')[0].astype(np.uint8)
print("running")
ser = serial.Serial('COM6',timeout=1)
ser.write(data)
ser.close()