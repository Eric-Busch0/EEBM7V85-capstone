
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import request
import json
import pickle
import numpy as np
from ecgdetectors import Detectors

filename = 'ecg_svm'
model = pickle.load(open(filename, 'rb'))


def get_predictions(ecg_data):
    fs = 360
    ts = 1 / 360
    detectors = Detectors(fs)
    r_peaks = detectors.pan_tompkins_detector(ecg_data)
    first_half = r_peaks[2:]
    first_half = np.multiply(np.array(ts), first_half)
    second_half = r_peaks[1 : -1]
    second_half = np.multiply(np.array(ts), second_half)

    pre_rr = np.subtract(first_half, second_half)
    post_rr = pre_rr[2:]

    post_rr = np.append([pre_rr[0], pre_rr[1]], post_rr)
    modelData = []
    for i in range(len(post_rr)):
        modelData.append([int(pre_rr[i] * 100), int(post_rr[i] * 100)])
    
    ans = model.predict(modelData)
    
    numNormal = 0
    numAbnormal = 0
    
    for i in ans:
        if i == 1:
            numNormal += 1
        else:
            numAbnormal += 1
    return {"normal" : numNormal, "abnormal" : numAbnormal}

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

 
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/',methods = ['POST'])
# ‘/’ URL is bound with hello_world() function.
def ml_predict():
    print("called")
    try:
        
        ret =request.get_json()['data']
        # print(ret)
        pred = get_predictions(ret)
        print(pred)
        return json.dumps(pred)
    
    except:
        # print(request.data)
        return "Error parsing"
    return 'Hello World'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=8000, host='0.0.0.0')